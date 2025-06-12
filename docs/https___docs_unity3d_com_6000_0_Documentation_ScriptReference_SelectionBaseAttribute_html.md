* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SelectionBaseAttribute.html

# SelectionBaseAttribute
class in UnityEngine
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
Add this attribute to a script class to mark its GameObject as a selection base object for Scene View picking.
In the Unity Scene View, when clicking to select objects, Unity will try to figure out the best object to select for you. If you click on an object that is part of a Prefab, the root of the Prefab is selected, because a Prefab root is treated as a selection base. You can make other objects be treated as selection base too. You need to create a script class with the SelectionBase attribute, and then you need to add that script to the GameObject.
* * *
