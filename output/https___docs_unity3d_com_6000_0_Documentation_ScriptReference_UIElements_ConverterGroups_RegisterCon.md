* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.RegisterConverterGroup.html

#  [ConverterGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroups.html).RegisterConverterGroup
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
public static void RegisterConverterGroup([UIElements.ConverterGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.ConverterGroup.html) converterGroup); 
### Parameters
Parameter | Description  
---|---  
converterGroup | The converter group to register.  
### Description
Registers a converter group by ID. Converter groups can be applied on a binding using local converters. 
You can apply a converter group in a [DataBinding](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DataBinding.html) UXML with the `source-to-ui-converters` or `ui-to-source-converters` attributes. 
* * *
