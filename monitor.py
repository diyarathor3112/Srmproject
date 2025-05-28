import psutil

def get_system_stats():
    return {
        'cpu': psutil.cpu_percent(interval=1),
        'ram': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'battery': psutil.sensors_battery().percent if psutil.sensors_battery() else None
    }
    import psutil
import platform
import time

def get_system_stats():
    stats = {}

    # CPU usage percentage (non-blocking)
    stats['cpu'] = psutil.cpu_percent(interval=1)

    # RAM usage percentage
    stats['ram'] = psutil.virtual_memory().percent

    # Disk usage percentage (root partition)
    stats['disk'] = psutil.disk_usage('/').percent

    # Battery percentage (None if no battery)
    battery = psutil.sensors_battery()
    stats['battery'] = battery.percent if battery else None

    # System uptime in seconds
    stats['uptime'] = time.time() - psutil.boot_time()

    # Number of running processes
    stats['process_count'] = len(psutil.pids())

    # OS name
    stats['os'] = platform.system()

    return stats
