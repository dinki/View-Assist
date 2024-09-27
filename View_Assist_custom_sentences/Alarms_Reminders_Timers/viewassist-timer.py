from datetime import datetime

def timerwait(duration, event_name, event_data, target_time):
    task.sleep (duration)

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
      days = secs//86400
      hours = (secs - days*86400)//3600
      minutes = (secs - days*86400 - hours*3600)//60
      seconds = secs - days*86400 - hours*3600 - minutes*60
      result = ("{0} day{1} and ".format(days, "s" if days!=1 else "") if days else "") + \
      ("{0} hour{1} and ".format(hours, "s" if hours!=1 else "") if hours else "") + \
      ("{0} minute{1} and ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
      ("{0} second{1}".format(seconds, "s" if seconds!=1 else "") if seconds else "")
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
