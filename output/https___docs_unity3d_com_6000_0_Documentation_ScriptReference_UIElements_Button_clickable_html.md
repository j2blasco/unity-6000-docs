* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button-clickable.html

#  [Button](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html).clickable
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
[UIElements.Clickable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.html) clickable; 
### Description
Clickable MouseManipulator for this Button. 
The default [Clickable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.html) object provides a list of actions that are called using one or more activation filters.   
  
To add or remove activation triggers, modify [clickable.activators](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseManipulator-activators.html). An activation trigger can be any mouse button, pressed any number of times, with any modifier key.   
  
Additional resources: [ManipulatorActivationFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ManipulatorActivationFilter.html)   
  

```
 myButton.clickable.activators.Add(new ManipulatorActivationFilter[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ManipulatorActivationFilter.html)(...))

```

```
myButton.clickable.activators.Clear()
```

* * *
