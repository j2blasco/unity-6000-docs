* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.UnbindProperties.html

#  [GenericBindingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html).UnbindProperties
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
public static void UnbindProperties(NativeArray<BoundProperty> boundProperties); 
### Parameters
Parameter | Description  
---|---  
boundProperties | The list of [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html) to unbind.  
### Description
Unbinds and frees all resources used by a list of [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html).
Creating a BoundProperty that targets a serialized reference avoids garbage collection for its objects. If you forget to unbind and free the resources used by this BoundProperty, it may result in a memory leak.  
  
This method throws an ArgumentException if the boundProperties's NativeArray is not yet created.
* * *
