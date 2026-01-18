import time

def measure_page_load(driver, url):
    start = time.time()
    driver.get(url)
    end = time.time()
    load_time = end - start
    print(f"[PERFORMANCE] Page '{url}' loaded in {load_time:.2f} seconds")
    return load_time

def measure_action_time(action_func, *args, **kwargs):
    start = time.time()
    action_func(*args, **kwargs)
    end = time.time()
    duration = end - start
    print(f"[PERFORMANCE] Action '{action_func.__name__}' took {duration:.2f} seconds")
    return duration

def measure_full_flow_times(actions_dict):
    results = {}
    for step, func in actions_dict.items():
        start = time.time()
        func()
        end = time.time()
        duration = end - start
        results[step] = duration
        print(f"[PERFORMANCE] Step '{step}' took {duration:.2f} seconds")
    return results
