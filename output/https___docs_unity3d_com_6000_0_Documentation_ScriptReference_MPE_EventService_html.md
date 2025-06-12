* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html

# EventService
class in UnityEditor.MPE
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
The EventService is a singleton implementation of a [ChannelClient](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.html) that runs on all instances of Unity. It is connected to the "events" channel and allows a Unity instance to send JSON messages to other [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html)s in external process, or other instances of Unity.
The [EventService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.html) can send fire-and-forget messages (see [EventService.Emit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Emit.html)), or request information or from a single client (see [EventService.Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Request.html)).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;
using UnityEditor.MPE;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
public static class EventServiceDocExample
{
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) s_CustomLogEventDisconnect;
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) s_PingPongEventDisconnect;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("EventServiceDoc/Step 0")]
    static void StartChannelService()
    {
        if (!ChannelService.IsRunning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.IsRunning.html)())
        {
            ChannelService.Start[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Start.html)();
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"[Step 0] ChannelService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html) Running: {ChannelService.GetAddress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetAddress.html)()}:{ChannelService.GetPort[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetPort.html)()}");
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("EventServiceDoc/Step 1")]
    static void SetupEventServiceHandlers()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("[Step 1] Setup handlers");
        s_CustomLogEventDisconnect = EventService.RegisterEventHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.RegisterEventHandler.html)("custom_log", (eventType, args) => {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Log a {eventType} {args[0]}");
        });  
  
        s_PingPongEventDisconnect = EventService.RegisterEventHandler[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.RegisterEventHandler.html)("pingpong", (eventType, args) =>
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Receive a {eventType} {args[0]}");
            return "pong!";
        });
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("EventServiceDoc/Step 2")]
    static void EmitMessage()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("[Step 2] Emitting a custom log");
        EventService.Emit[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Emit.html)("custom_log", "Hello world!", -1, EventDataSerialization.JsonUtility[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventDataSerialization.JsonUtility.html));
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("EventServiceDoc/Step 3")]
    static void SendRequest()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("[Step 3] Sending a request");
        EventService.Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Request.html)("pingpong", (err, data) =>
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) fulfilled: {data[0]}");
        },
            "ping", -1, EventDataSerialization.JsonUtility[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventDataSerialization.JsonUtility.html));
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("EventServiceDoc/Step 4")]
    static void CloseHandlers()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("[Step 4] Closing all Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) handlers");
        s_CustomLogEventDisconnect();
        s_PingPongEventDisconnect();
    }
}  
  
/*  
  
When you execute the five menu items one after the other, Unity prints the following messages to the Console window:  
  
[Step 0] ChannelService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html) Running: 127.0.0.1:65000  
  
[Step 1] Setup handlers  
  
[Step 2] Emitting a custom log  
  
Log a custom_log Hello world!  
  
[Step 3] Sending a request  
  
Receive a pingpong ping  
  
Request[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html) fulfilled: pong!  
  
[Step 4] Closing all Event[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) handlers  
  
*/

```

### Static Properties
Property | Description  
---|---  
[isConnected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService-isConnected.html) | The EventService connected to the ChannelService's "events" channel.  
### Static Methods
Method | Description  
---|---  
[CancelRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.CancelRequest.html) | Checks whether there is a pending request for a specific event and, if there is, cancels it. See EventService.Request for more details on Request.  
[Clear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Clear.html) | Clear all pending Requests.  
[Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Close.html) | Closes the EventService, terminates connections to the ChannelService, and ensures that no more handlers are processed.  
[Emit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Emit.html) | Sends a fire-and-forget message to all ChannelClients connected to the "events" route.  
[IsRequestPending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.IsRequestPending.html) | Checks whether a request is pending on a specific event. For more information about Request, see EventService.Request.  
[Log](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Log.html) | Sends a log message to the ChannelService. Log messages are printed to the Console window.  
[RegisterEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.RegisterEventHandler.html) | Registers a handler for a specific event type. The handler is called whenever a message of the specified type is sent. Messages are sent using EventService.Emit or EventService.Request.  
[Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Request.html) | Sends a request to all connected clients on the "events" channel.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Start.html) | Starts the EventService so it listens to new messages.  
[Tick](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.Tick.html) | Ticks the EventService. This processes all incoming and outgoing messages. By default, the EventService is ticked on each EditorApplication.update.  
[UnregisterEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.EventService.UnregisterEventHandler.html) | Unregisters a handler from a specific event.  
* * *
