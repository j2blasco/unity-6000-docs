* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CustomPropertyDrawer-ctor.html

# CustomPropertyDrawer Constructor
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
public CustomPropertyDrawer(Type type); 
## Declaration
public CustomPropertyDrawer(Type type, bool useForChildren); 
### Parameters
Parameter | Description  
---|---  
type | If the drawer is for a custom Serializable class, the type should be that class. If the drawer is for script variables with a specific [PropertyAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyAttribute.html), the type should be that attribute.  
useForChildren | If true, the drawer will be used for any children of the specified class unless they define their own drawer.  
### Description
Tells a PropertyDrawer or DecoratorDrawer class which run-time class or attribute it's a drawer for.
When you make a custom drawer, you need put this attribute on the drawer class.  
  
Additional resources: [PropertyDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PropertyDrawer.html) class, [DecoratorDrawer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DecoratorDrawer.html) class.
* * *
