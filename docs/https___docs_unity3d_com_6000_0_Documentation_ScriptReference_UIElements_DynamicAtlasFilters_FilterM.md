* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.FilterMode.html

#  [DynamicAtlasFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.DynamicAtlasFilters.html).FilterMode
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
### Description
Excludes textures that use a filter mode that the atlas does not support.  
  
This filter is disabled by default. You can enable it to prevent artifacts that might occur when the atlas does not support the texture's filter mode, and cannot sample the texture correctly. However, because excluding textures from the atlas can reduce performance, the default behavior is preferable in most cases.  
  
On GLES3 (and later) devices, the atlas supports more than one filter mode, so you should not need to enable this filter. 
* * *
