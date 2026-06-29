def task_status():
    status="pending"
    def complete():
        nonlocal status
        status="completed"
    complete()
    print("Final Status:",status)
task_status()
