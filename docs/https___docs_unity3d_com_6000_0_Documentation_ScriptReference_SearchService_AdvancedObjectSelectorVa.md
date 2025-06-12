* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.AdvancedObjectSelectorValidatorAttribute-ctor.html

# AdvancedObjectSelectorValidatorAttribute Constructor
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
public AdvancedObjectSelectorValidatorAttribute(string id); 
### Parameters
Parameter | Description  
---|---  
id | A unique identifier for this advanced object selector validator.  
### Description
Registers a method to act as an advanced object selector validator.
A unique identifier is required when registering a custom advanced object selector validator. If the identifier is not unique, the advanced object selector validator is not registered and a warning is displayed in the console. The same identifier must be used by the attribute [AdvancedObjectSelectorAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.AdvancedObjectSelectorAttribute.html) to properly register an advanced object selector.
* * *
