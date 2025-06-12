* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html

# ChannelService
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
The ChannelService encapsulates a WebSocket server running in Unity.
The ChannelService allows you to create new communication channels. A channel matches the route of the URL connecting to the ChannelService. For example, "127.0.0.1:9292/<channelName>"  
  
The ChannelService allows custom handlers to receive all messages on a specific channel.  
  
Unity does not start the ChannelService automatically. You must start it manually using [ChannelService.Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Start.html). Alternatively, you can use the following command line switch: --ump-channel-service-on-startup.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Text;
using UnityEditor.MPE;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEngine;  
  
public static class ChannelCommunicationDocExample
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ChannelDoc/Step 1")]
    static void StartChannelService()
    {
        if (!ChannelService.IsRunning[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.IsRunning.html)())
        {
            ChannelService.Start[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Start.html)();
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"[Step1] ChannelService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html) Running: {ChannelService.GetAddress[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetAddress.html)()}:{ChannelService.GetPort[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetPort.html)()}");
    }  
  
    static int s_BinaryChannelId;
    static int s_StringChannelId;
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) s_DisconnectBinaryChannel;
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) s_DisconnectStringChannel;  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ChannelDoc/Step 2")]
    static void SetupChannelService()
    {
        if (s_DisconnectBinaryChannel == null)
        {
            s_DisconnectBinaryChannel = ChannelService.GetOrCreateChannel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetOrCreateChannel.html)("custom_binary_ping_pong", HandleChannelBinaryMessage);
            s_BinaryChannelId = ChannelService.ChannelNameToId[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.ChannelNameToId.html)("custom_binary_ping_pong");
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"[Step2] Setup channel_custom_binary id: {s_BinaryChannelId}");  
  
        if (s_DisconnectStringChannel == null)
        {
            s_DisconnectStringChannel = ChannelService.GetOrCreateChannel[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetOrCreateChannel.html)("custom_ascii_ping_pong", HandleChannelStringMessage);
            s_StringChannelId = ChannelService.ChannelNameToId[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.ChannelNameToId.html)("custom_ascii_ping_pong");
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"[Step2] Setup channel_custom_ascii id: {s_StringChannelId}");
    }  
  
    static void HandleChannelBinaryMessage(int connectionId, byte[] data)
    {
        var msg = "";
        for (var i = 0; i < Math.Min(10, data.Length); ++i)
        {
            msg += data[i].ToString();
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Channel Handling binary from connection {connectionId} - {data.Length} bytes - {msg}");  
  
        // Client[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) has sent a message (this is a ping)
        // Lets send back the same message (as a pong)
        ChannelService.Send[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Send.html)(connectionId, data);
    }  
  
    static void HandleChannelStringMessage(int connectionId, byte[] data)
    {
        // Client[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) has sent a message (this is a ping)
        // Client[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) expects string data. Encode the data and send it back as a string:  
  
        var msgStr = Encoding.UTF8.GetString(data);
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Channel Handling string from connection {connectionId} - {msgStr}");  
  
        // Send back the same message (as a pong)
        ChannelService.Send[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Send.html)(connectionId, msgStr);
    }  
  
    static ChannelClient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.html) s_BinaryClient;
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) s_DisconnectBinaryClient;
    static ChannelClient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.html) s_StringClient;
    static Action[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) s_DisconnectStringClient;
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ChannelDoc/Step 3")]
    static void SetupChannelClient()
    {
        const bool autoTick = true;  
  
        if (s_BinaryClient == null)
        {
            s_BinaryClient = ChannelClient.GetOrCreateClient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.GetOrCreateClient.html)("custom_binary_ping_pong");
            s_BinaryClient.Start(autoTick);
            s_DisconnectBinaryClient = s_BinaryClient.RegisterMessageHandler(HandleClientBinaryMessage);
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"[Step3] Setup client for channel custom_binary_ping_pong. ClientId: {s_BinaryClient.clientId}");  
  
        if (s_StringClient == null)
        {
            s_StringClient = ChannelClient.GetOrCreateClient[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelClient.GetOrCreateClient.html)("custom_ascii_ping_pong");
            s_StringClient.Start(autoTick);
            s_DisconnectStringClient = s_StringClient.RegisterMessageHandler(HandleClientStringMessage);
        }
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"[Step3] Setup client for channel custom_ascii_ping_pong. ClientId: {s_StringClient.clientId}");
    }  
  
    static void HandleClientBinaryMessage(byte[] data)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Receiving pong binary data: {data} for clientId: {s_BinaryClient.clientId} with channelName: {s_BinaryClient.channelName}");
    }  
  
    static void HandleClientStringMessage(string data)
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Receiving pong data: {data} for clientId: {s_StringClient.clientId} with channelName: {s_StringClient.channelName}");
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ChannelDoc/Step 4")]
    static void ClientSendMessageToServer()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("[Step 4]: Clients are sending data!");
        s_BinaryClient.Send(new byte[] { 0, 1, 2, 3, 4, 5, 6, 7 });
        s_StringClient.Send("Hello world!");
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ChannelDoc/Step 5")]
    static void CloseClients()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("[Step 5]: Closing clients");
        s_DisconnectBinaryClient();
        s_BinaryClient.Close();  
  
        s_DisconnectStringClient();
        s_StringClient.Close();
    }  
  
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("ChannelDoc/Step 6")]
    static void CloseService()
    {
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("[Step 6]: Closing clients");  
  
        s_DisconnectBinaryChannel();
        s_DisconnectStringChannel();  
  
        ChannelService.Stop[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Stop.html)();
    }
}  
  
/*
When you execute the menu items one after the other, Unity prints the following messages to the Console window:  
  
[Step1] ChannelService[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html) Running: 127.0.0.1:64647  
  
[Step2] Setup channel_custom_binary id: -1698345965  
  
[Step2] Setup channel_custom_ascii id: -930064725  
  
[Step3] Setup client for channel custom_binary_ping_pong. ClientId: -1698345965  
  
[Step3] Setup client for channel custom_ascii_ping_pong. ClientId: -930064725  
  
[Step 4]: Clients are sending data!  
  
Channel Handling binary from connection 1 - 8 bytes - 01234567  
  
Channel Handling string from connection 2 - Hello world!  
  
Receiving pong binary data: System.Byte[] for clientId: -1698345965 with channelName: custom_binary_ping_pong  
  
Receiving pong data: Hello world! for clientId: -930064725 with channelName: custom_ascii_ping_pong  
  
[Step 5]: Closing clients  
  
[Step 6]: Closing clients  
  
*/

```

### Static Methods
Method | Description  
---|---  
[Broadcast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Broadcast.html) | Sends a message to all of a specific channel's ChannelClient connections.  
[BroadcastBinary](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.BroadcastBinary.html) | Sends a message to all of a specific channel's ChannelClient connections.  
[ChannelNameToId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.ChannelNameToId.html) | Closes a specific channel and all connections to that channel.  
[CloseChannel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.CloseChannel.html) | Closes a specific channel and all connections to that channel.  
[DispatchMessages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.DispatchMessages.html) | Dispatches any messages that have been received since the last dispatch. This happens automatically every editor tick, but this method can be used to force dispatching to occur during thread-blocking operations.  
[GetAddress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetAddress.html) | Gets the address of the ChannelService. This is always a local address. For example, 127.0.0.1.  
[GetChannelClientList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetChannelClientList.html) | Gets a list of all channel clients connected to the ChannelService.  
[GetChannelList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetChannelList.html) | Gets a list of channels open in the ChannelService. By default the ChannelService always has a "status" channel and an "events" channel.  
[GetOrCreateChannel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetOrCreateChannel.html) | Gets or creates a new channel.  
[GetPort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetPort.html) | Retrieves the port where the ChannelService runs. This port is chosen randomly when the ChannelService first starts. Alternatively you can specify the port from the command line, using the --ump-channel-service-port <portNumber> switch.  
[IsRunning](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.IsRunning.html) | Checks whether the ChannelService is running and listening to new connections..  
[RegisterMessageHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.RegisterMessageHandler.html) | Registers a handler to process all incoming messages on a specific channel.  
[Send](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Send.html) | Sends a message to a specific connection. The message can be binary or UTF8.  
[Start](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Start.html) | Starts the ChannelService. After you start the ChannelService it listens to connection at the URL provided by: <ChannelService Address>:<ChannelServicePort>/<channelName>, for example, 127.0.0.1:9976/events. See ChannelService.GetAddress and ChannnelService.GetPort.  
[Stop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.Stop.html) | Stops the ChannelService from listening to connections, and closes any already established connections.  
[UnregisterMessageHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.UnregisterMessageHandler.html) | Unregisters a specific handler from a Channel.  
* * *
