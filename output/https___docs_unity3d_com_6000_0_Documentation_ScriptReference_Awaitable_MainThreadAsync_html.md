* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.MainThreadAsync.html

#  [Awaitable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html).MainThreadAsync
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
public static MainThreadAwaitable MainThreadAsync(); 
### Returns
**MainThreadAwaitable** Awaitable object that completes when switching to the main thread. 
### Description
Resumes execution on the Unity main thread. Completes immediately when called from the main thread.
```
public async Awaitable[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.html) Start()
{
    await Awaitable.BackgroundThreadAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.BackgroundThreadAsync.html)();
    // do some heavy math here without blocking the frame
    float result = 42;
    // switch back to the main frame to be able to call SceneManager.LoadSceneAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html)
    await Awaitable.MainThreadAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Awaitable.MainThreadAsync.html)();
    await SceneManager.LoadSceneAsync[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.SceneManager.LoadSceneAsync.html)("my-scene");
}

```

* * *
