* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.DispatchMessages.html

#  [ChannelService](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MPE.ChannelService.html).DispatchMessages
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
public static void DispatchMessages(); 
### Description
Dispatches any messages that have been received since the last dispatch. This happens automatically every editor tick, but this method can be used to force dispatching to occur during thread-blocking operations.
* * *
