* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.SetValues.html

#  [GenericBindingUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.GenericBindingUtility.html).SetValues
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
public static void SetValues(NativeArray<BoundProperty> boundProperties, NativeArray<float> values); 
## Declaration
public static void SetValues(NativeArray<BoundProperty> boundProperties, NativeArray<int> values); 
### Parameters
Parameter | Description  
---|---  
boundProperties | The list of [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html) to set the values for.  
values | The list of float or integer values to set.  
### Description
Sets the float or integer value for each [[BoundProperty].
This method throws an ArgumentException if the NativeArray is not yet created.  
  
This method throws an ArgumentException if the indices list does not match the length of the boundProperties list.
* * *
## Declaration
public static void SetValues(NativeArray<BoundProperty> boundProperties, NativeArray<int> indices, NativeArray<float> values); 
## Declaration
public static void SetValues(NativeArray<BoundProperty> boundProperties, NativeArray<int> indices, NativeArray<int> values); 
### Parameters
Parameter | Description  
---|---  
boundProperties | The list of [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html) to set the values for.  
indices | The list of indices where each [BoundProperty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Animations.BoundProperty.html) value will be read.  
values | The list of float or integer values.  
### Description
Sets the float/integer values for each [[BoundProperty] and uses the value at the index define in indices.
This method throws an ArgumentException if the NativeArray is not yet created.  
  
This method throws an ArgumentException if the indices list does not match the length of the boundProperties list.  
  
This method throws an IndexOutOfRangeException if an index in the indices list is out of range.
* * *
