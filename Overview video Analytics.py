from gtts import gTTS
import os
from datetime import datetime
 
# ---- Step 1: Dynamic Summary Input ----
# You can replace this with text from a report, dashboard, or AI output
summary = """
Good afternoon. Welcome to the central security overview dashboard. This gives us a real-time, high-level summary of our entire surveillance network.

As you can see from the top-line metrics, we currently have 50 active cameras online. These have registered a total of 200 events so far today across our 19 active zones.

I want to immediately draw your attention to the 'System Health' status. While we have 50 cameras online, the system is flagging 18 as 'Offline'. This is a priority for our technical team to investigate. Correspondingly, our storage utilization is getting high, so we'll need to monitor that as well.

To the right of the live feeds, the 'Object & Face Analytics' chart shows a breakdown of what the system is detecting. The primary detections are people, with a count of nearly 600, followed by about 200 vehicles.

The 'Event Detection and Alerts' log is where we see these analytics in action. For example, if we look at the events from this morning, September 5th, 2025, we can see a cluster of activity between 8:00 AM and 8:10 AM. There were multiple 'Intrusion' alerts from camera CAM041 in the 'Meeting Area', followed by an 'Object Disappearance' alert from that same camera. This is a sequence of events we need to review immediately.

Drilling down, the 'Camera Performance Metrics' table gives us granular detail on each device. We can confirm, for instance, that the 'Archive Room' camera is listed with a 'Disconnected' network status, likely one of our 18 offline devices. We can also see which cameras have face detection or infrared enabled.

The 'System Health Controller' panel shows the status of our access points, with most online and active. The 'Layout Map' gives us a visual heat map of our zones, and finally, the 'Face Detection' donut chart shows that of the 52 faces detected today, the system has identified 44 as male and 8 as female.

In summary, the key takeaways are to address the offline cameras and to urgently investigate the intrusion and object disappearance alerts from the Meeting Area this morning.
"""
 
# ---- Step 2: Convert Summary to Audio ----
# Use current timestamp for dynamic file name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
audio_filename = f"Overview{timestamp}.mp3"
 
# Generate audio using gTTS (Google Text-to-Speech)
tts = gTTS(text=summary, lang='en')
tts.save(audio_filename)
 
print(f"✅ Audio summary saved as: {audio_filename}")
 
# ---- Optional: Play the Audio ----
try:
    from playsound import playsound
    playsound(audio_filename)
except:
    print("🔊 Audio playback skipped. Install 'playsound' if needed.")