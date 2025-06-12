* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable-clicked.html

#  [Clickable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Clickable.html).clicked
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
Callback triggered when the target element is clicked. 
Encapsulates a method that has no parameters and does not return a value.   
  

```
 public VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreateButton()
 {
     var button = new Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) { text = "Press Me" };
     button.clicked += () =>
     {
         Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Button[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Button.html) was pressed!");
     };
     return button;
 }

```

* * *
