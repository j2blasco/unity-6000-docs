* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.html

# RuntimeInitializeLoadType
enumeration
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
Specifies when to get a callback during the startup of the runtime or when entering play mode in the Editor. Used with [RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html).
See the [RuntimeInitializeOnLoadMethodAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeOnLoadMethodAttribute.html) documentation for the execution order between the various options.
### Properties
Property | Description  
---|---  
[AfterSceneLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.AfterSceneLoad.html) | Callback invoked when the first scene's objects are loaded into memory and after Awake has been called.  
[BeforeSceneLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.BeforeSceneLoad.html) | Callback invoked when the first scene's objects are loaded into memory but before Awake has been called.  
[AfterAssembliesLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.AfterAssembliesLoaded.html) | Callback invoked when all assemblies are loaded and preloaded assets are initialized. At this time the objects of the first scene have not been loaded yet.  
[BeforeSplashScreen](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.BeforeSplashScreen.html) | Callback invoked before the splash screen is shown. At this time the objects of the first scene have not been loaded yet.  
[SubsystemRegistration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RuntimeInitializeLoadType.SubsystemRegistration.html) | Callback invoked when starting up the runtime. Called before the first scene is loaded.  
* * *
