* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter-isPreloaded.html

#  [PluginImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PluginImporter.html).isPreloaded
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
isPreloaded; 
### Description
Is a native plugin loaded during startup or on demand?
You can use this to ensure that a plugin is loaded early in the startup phase instead of on first use.  
  
Plugins whose names are prefixed with one of the following strings are configured to be preloaded by default: AudioPlugin, libAudioPlugin, GfxPlugin, libGfxPlugin, ProfilerPlugin, libProfilerPlugin.  
  
Note: Preloading is only supported for native plugins. 
* * *
