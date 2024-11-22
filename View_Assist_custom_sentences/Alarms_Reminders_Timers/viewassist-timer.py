from datetime import datetime, timedelta
import re

# Dictionary to map words to numbers
word_to_num = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10
}

# Convert the time description into seconds
def time_to_seconds(time_description: str) -> int:
    # Replace words with numbers
    for word, num in word_to_num.items():
        time_description = re.sub(rf'\b{word}\b', str(num), time_description)

    # Regex to extract numeric value and time unit
    pattern = re.compile(r'(\d+)\s*(second|minute|hour|day|week|month|year)s?')
    total_seconds = 0

    # Match and calculate total seconds
    for match in pattern.finditer(time_description):
        value = int(match.group(1))
        unit = match.group(2)

        if unit == "second":
            total_seconds += value
        elif unit == "minute":
            total_seconds += value * 60
        elif unit == "hour":
            total_seconds += value * 3600
        elif unit == "day":
            total_seconds += value * 86400
        elif unit == "week":
            total_seconds += value * 604800
        elif unit == "month":
            total_seconds += value * 2628000  # Assuming 1 month = 30.44 days
        elif unit == "year":
            total_seconds += value * 31536000  # Assuming 1 year = 365 days

    return total_seconds

def timerwait(duration, event_name, event_data, target_time):
    task.sleep(duration)
    # Fire the event
    event.fire(event_name, **event_data)
    log.warning(f"Event '{event_name}' fired at {target_time}")    

@service
def schedule_event_at_time(event_name: str, event_data: dict = {}, target_time: str = ""):
    """yaml
    name: View Assist Schedule Event at Time
    description: Used for timers to schedule an event broadcast for a certain time
    """
    # Parse the target time from the input string
    target_time = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
    
    # Get the current time
    now = datetime.now()
    
    # Calculate the sleep duration
    sleep_duration = (target_time - now).total_seconds()
    
    # Wait until the target time
    task.create(timerwait, sleep_duration, event_name, event_data, target_time)

@service(supports_response="optional")
def get_time_difference(target_time: str = "") -> dict:
    """yaml
    name: View Assist Get Time Difference
    description: Returns a human readable time difference between a given time and now
    """  
    def secondsToText(secs):
        days = secs // 86400
        hours = (secs - days * 86400) // 3600
        minutes = (secs - days * 86400 - hours * 3600) // 60
        seconds = secs - days * 86400 - hours * 3600 - minutes * 60
        result = ("{0} day{1} and ".format(days, "s" if days != 1 else "") if days else "") + \
                 ("{0} hour{1} and ".format(hours, "s" if hours != 1 else "") if hours else "") + \
                 ("{0} minute{1} and ".format(minutes, "s" if minutes != 1 else "") if minutes else "") + \
                 ("{0} second{1}".format(seconds, "s" if seconds != 1 else "") if seconds else "")
        return result
  
    # Parse the target time from the input string
    target_time = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")
    
    # Get the current time
    now = datetime.now()
    
    # Calculate the difference in seconds
    time_difference = round((target_time - now).total_seconds())
    time_difference = secondsToText(time_difference)
    
    # Log the time difference
    log.warning(f"Time difference for target time '{target_time}': {time_difference} seconds")
    
    # Return the time difference in a dictionary
    return {"time_difference": time_difference}

@service(supports_response="optional")
def convert_to_seconds(time_when: str = "") -> dict:
    """yaml
    name: View Assist Convert Time to Seconds
    description: Converts a human-readable time description like 'one minute' or '20 seconds' to seconds
    """
    total_seconds = time_to_seconds(time_when)
    
    log.warning(f"Converted '{time_when}' to {total_seconds} seconds")
    
    # Return the total seconds in a dictionary
    return {"total_seconds": total_seconds}

@service
def broadcast_event(event_name: str, event_data: dict = {}):
    """yaml
    name: View Assist Broadcast Event
    description: Immediately fires an event with the provided name and data
    """
    # Fire the event
    event.fire(event_name, **event_data)
    log.warning(f"Event '{event_name}' fired with data: {event_data}")

