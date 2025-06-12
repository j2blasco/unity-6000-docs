* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.html

# SceneTemplateService
class in UnityEditor.SceneTemplate
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
A utility class that manages [SceneTemplateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateAsset.html) instantiation.
### Static Methods
Method | Description  
---|---  
[CreateSceneTemplate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.CreateSceneTemplate.html) | Creates a new Scene template at a specific path. The template is not bound to a Scene.  
[CreateTemplateFromScene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.CreateTemplateFromScene.html) | Creates a new Scene template bound to a specific Scene. All of the template Scene's dependencies are extracted and set to be referenced.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.Instantiate.html) | Instantiates a new Scene from a template.  
### Events
Event | Description  
---|---  
[newSceneTemplateInstantiated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService-newSceneTemplateInstantiated.html) | Events fired after a Scene template is instantiated.  
[newSceneTemplateInstantiating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService-newSceneTemplateInstantiating.html) | Events fired before a Scene template is instantiated.  
### Delegates
Delegate | Description  
---|---  
[NewTemplateInstantiated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.NewTemplateInstantiated.html) | An event called after a Scene template is instantiated.  
[NewTemplateInstantiating](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneTemplate.SceneTemplateService.NewTemplateInstantiating.html) | An event called before a Scene template is instantiated.  
* * *
