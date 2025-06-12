* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.RegisterGlobalConverter.html

#  [ConverterGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.html).RegisterGlobalConverter
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
public static void RegisterGlobalConverter(TypeConverter<TSource,TDestination> converter); 
### Parameters
Parameter | Description  
---|---  
converter | The delegate that handles the conversion.  
### Description
Registers a global UI conversion delegate that will be used when converting data between a data source and a UI control. This delegate will be used both when converting data from and to UI. 
* * *
