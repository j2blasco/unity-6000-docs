* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/mobile-accessibility.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * Accessibility for mobile applications


[](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildPlayerPipeline.html)
Build Player Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html)
Unity Remote
# Accessibility for mobile applications
Use the [Accessibility module APIs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AccessibilityModule.html) to create mobile applications that are accessible to a wider audience, including people with disabilities.
## Requirements and compatibility
The Accessibility module APIs are available only for iOS and Android devices, with the following minimum requirements:
**Platform** | **Operating system version**  
---|---  
**Android** | Android 8.0 (API level 26)  
**iOS** | iOS 13  
## Screen reader support
Android and iOS devices have built-in screen readers that describe what appears on the screen out loud. These screen readers are designed to help users who are blind or have low vision to navigate and interact with their mobile devices without needing to see the screen. 
**Platform** | **Screen reader**  
---|---  
**Android** | [VoiceOver](https://developer.apple.com/documentation/accessibility/voiceover)  
**iOS** | [TalkBack](https://support.google.com/accessibility/android/topic/10601571?hl=en-GB&ref_topic=3529932)  
Use Unity’s [Assistive Support API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AssistiveSupport.html) to enable screen reader capabilities for your application. The `AssistiveSupport` class stores the active accessibility hierarchy that you create, allows your application to notify the screen reader of changes in your UI, and notifies your application of events based on user actions. Use the **Accessibility Hierarchy Viewer** (menu: **Window** > **Accessibility** > **Accessibility Hierarchy Viewer**) during Play mode to view the active accessibility hierarchy and its nodes in real-time.
## System settings
Use Unity’s [Accessibility Settings API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Accessibility.AccessibilitySettings.html) to configure your UI to interact with native font scaling, bold text, and closed captions. This improves the readability and visibility of your application’s UI for all your users.
## Additional resources
  * [Accessibility Public Sample: LetterSpell](https://github.com/Unity-Technologies/a11y-public-sample) on GitHub
  * [Accessibility module](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.AccessibilityModule.html) API documentation
  * [Mobile screen reader support in Unity](https://unity.com/blog/engine-platform/mobile-screen-reader-support-in-unity)
  * [Unity Discussions: Accessibility](https://discussions.unity.com/tag/Accessibility)
  * [User interfaces roadmap](https://unity.com/roadmap/unity-platform/ui)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildPlayerPipeline.html)
Build Player Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityRemote5.html)
Unity Remote
