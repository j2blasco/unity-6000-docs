* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearch.RegisterEngine.html

#  [ObjectSelectorSearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearch.html).RegisterEngine
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
public static void RegisterEngine([SearchService.IObjectSelectorEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.IObjectSelectorEngine.html) engine); 
### Parameters
Parameter | Description  
---|---  
engine | The ObjectSelector search engine to register.  
### Description
Registers an ObjectSelector search engine dynamically.
If you set a dynamically registered engine as the active search engine via the Settings window, you must make sure to register it in subsequent Unity sessions before it is used. If you do not register it, Unity reverts to the default search engine.  
  
Additional resources: [ObjectSelectorSearch.UnregisterEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SearchService.ObjectSelectorSearch.UnregisterEngine.html).
* * *
