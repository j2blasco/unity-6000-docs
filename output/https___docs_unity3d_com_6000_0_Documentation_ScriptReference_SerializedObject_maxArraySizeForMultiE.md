* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject-maxArraySizeForMultiEditing.html

#  [SerializedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedObject.html).maxArraySizeForMultiEditing
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
maxArraySizeForMultiEditing; 
### Description
Defines the maximum size beyond which arrays cannot be edited when multiple objects are selected.
This value controls the maximum array size that you can edit during multiple-object-editing in the Inspector.  
  
When you select two or more GameObjects and the minimum array size for a property is larger than this value, the Inspector shows an empty array and [SerializedProperty.arraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-arraySize.html) returns 0. In that case, [SerializedProperty.minArraySize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SerializedProperty-minArraySize.html) exposes the actual minimum size.  
  
As a compromise between performance and utility, the default array size is 64.  
  
If your serialized object typically has arrays larger than this, you can set this value to a higher number to allow multi-editing on those arrays. Please be aware that setting too high a value might affect Inspector performance when editing large arrays or a large number of objects.
* * *
