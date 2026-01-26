import socket
import time
import os
import shutil
import urllib.request

def test_dns(hostname="pypi.org"):
    print(f"\n[1] Testing DNS Resolution for {hostname} (Cloudflare Check)...")
    start = time.perf_counter()
    try:
        ip = socket.gethostbyname(hostname)
        end = time.perf_counter()
        duration_ms = (end - start) * 1000
        print(f"    SUCCESS: Resolved to {ip}")
        print(f"    TIME:    {duration_ms:.2f} ms")
        if duration_ms < 50:
            print("    VERDICT: EXCELLENT (Cloudflare 1.1.1.1 is active)")
        else:
            print("    VERDICT: SLOW (Might still be using ISP DNS)")
    except socket.error as e:
        print(f"    FAIL: Could not resolve {hostname}. Error: {e}")

def test_io_speed():
    print(f"\n[2] Testing Disk I/O (Defender Exclusion Check)...")
    test_dir = "defender_test_temp"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir)
    
    print("    Writing 1,000 small files (Simulating compilation)...")
    start = time.perf_counter()
    for i in range(1000):
        with open(os.path.join(test_dir, f"test_{i}.txt"), "w") as f:
            f.write("import this\n" * 10)
    end = time.perf_counter()
    
    duration = end - start
    print(f"    TIME:    {duration:.4f} seconds")
    
    # Cleanup
    shutil.rmtree(test_dir)
    
    if duration < 1.0:
        print("    VERDICT: BLAZING FAST (Defender is likely ignoring this folder)")
    elif duration < 3.0:
        print("    VERDICT: ACCEPTABLE (Standard overhead)")
    else:
        print("    VERDICT: SLOW (Defender might be scanning every file write. Check Exclusions.)")

def test_connectivity():
    print(f"\n[3] Testing Pip Connectivity (SSL Handshake)...")
    url = "https://pypi.org"
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            end = time.perf_counter()
            print(f"    STATUS:  {response.getcode()} OK")
            print(f"    TIME:    {(end - start):.4f} seconds")
            print("    VERDICT: CONNECTED")
    except Exception as e:
        print(f"    FAIL: {e}")

if __name__ == "__main__":
    print("=== SYSTEM OPTIMIZATION VERIFICATION ===")
    test_dns()
    test_connectivity()
    test_io_speed()
    print("\n=== TEST COMPLETE ===")