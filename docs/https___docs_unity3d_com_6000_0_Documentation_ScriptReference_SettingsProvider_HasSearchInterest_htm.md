* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.HasSearchInterest.html

#  [SettingsProvider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider.html).HasSearchInterest
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
public bool HasSearchInterest(string searchContext); 
### Parameters
Parameter | Description  
---|---  
searchContext | Search terms that the user entered in the search box on the Settings window.  
### Returns
**bool** True if the SettingsProvider matched the search term and if it should appear. 
### Description
Checks whether the SettingsProvider should appear when the user types something in the Settings window search box. SettingsProvider tries to match the search terms (even partially) to any of the [SettingsProvider.keywords](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SettingsProvider-keywords.html). The search is case insensitive.
* * *
