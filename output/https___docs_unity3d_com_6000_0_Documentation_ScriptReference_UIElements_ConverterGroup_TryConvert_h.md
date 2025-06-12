* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.TryConvert.html

#  [ConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.html).TryConvert
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
public bool TryConvert(ref TSource source, out TDestination destination); 
### Parameters
Parameter | Description  
---|---  
source | The source value to convert.  
destination | The converted destination value if the conversion succeeded, and the default value otherwise.  
### Returns
**bool** `true` if the conversion succeeded, and `false` otherwise. 
### Description
Converts the specified value from `TSource` to `TDestination` using only the converter group. 
* * *
