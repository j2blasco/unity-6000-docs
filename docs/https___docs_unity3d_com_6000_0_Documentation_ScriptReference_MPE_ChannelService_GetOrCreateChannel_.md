* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.GetOrCreateChannel.html

#  [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).GetOrCreateChannel
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
## Declaration
public static [Unity.Android.Gradle.Manifest.Action](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Android.Gradle.Manifest.Action.html) GetOrCreateChannel(string channelName, Action<int,byte[]> handler); 
### Parameters
Parameter | Description  
---|---  
channelName | The name of the channel to retrieve.  
handler | The channel handler to register.  
### Returns
**Action** This action can be invoked to unregister the handler from the channel (see [ChannelService.UnregisterMessageHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.UnregisterMessageHandler.html)). 
### Description
Gets or creates a new channel.
When you create a channel, the ChannelService listens to connections on it, and routes all messages sent to it. You have to register a handler to process the messages and send them back to other clients."  
  
If a channel with the same name already exists, it appends the handler to its list of handlers. This allows you to log or listen to all messages sent to a specific channel.
* * *
