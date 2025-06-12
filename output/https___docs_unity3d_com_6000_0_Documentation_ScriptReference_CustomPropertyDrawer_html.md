* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPropertyDrawer.html

# CustomPropertyDrawer
class in UnityEditor
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
Tells a custom [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) or [DecoratorDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html) which run-time Serializable class or [PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html) it's a drawer for.
When you make a custom [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) or [DecoratorDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html), you need put this attribute on the drawer class. If the drawer is for a Serializable class, then pass the type of the class to the CustomPropertyDrawer attribute (only valid for PropertyDrawers; not DecoratorDrawers). If the drawer is for a [PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html), then pass the type of the PropertyAttribute to the CustomPropertyDrawer attribute.  
  
Additional resources: [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) class, [DecoratorDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html) class.
### Constructors
Constructor | Description  
---|---  
[CustomPropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPropertyDrawer-ctor.html) | Tells a PropertyDrawer or DecoratorDrawer class which run-time class or attribute it's a drawer for.  
* * *
