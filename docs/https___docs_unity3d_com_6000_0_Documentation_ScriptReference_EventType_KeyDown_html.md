* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.KeyDown.html

#  [EventType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventType.html).KeyDown
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
A keyboard key was pressed.
Use [Event.character](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-character.html) to find out what has been typed. Use [Event.keyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-keyCode.html) to handle arrow, home/end or other function keys, or to find out which physical key has been pressed. This event is sent repeatedly depending on the end user's keyboard repeat settings.  
  
Note that key presses can come as separate events, one with valid [Event.keyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-keyCode.html), and another with valid [Event.character](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-character.html). In case of keyboard layouts with dead keys, multiple [Event.keyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-keyCode.html) events can generate a single [Event.character](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event-character.html) event.
* * *
