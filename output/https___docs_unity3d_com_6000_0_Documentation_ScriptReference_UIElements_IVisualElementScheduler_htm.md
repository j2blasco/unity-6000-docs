* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduler.html

# IVisualElementScheduler
interface in UnityEngine.UIElements
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
A scheduler provides the functionality to queue actions to run at a specific time or duration. 
You can use the scheduler to create animations, update the UI, or create tasks that require a delay or repeated action.   
  
To schedule an action, use the [IVisualElementScheduler.Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduler.Execute.html) method. The scheduler runs the action at the next frame.   
  
A [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) associates with the scheduler, which you can access through the [VisualElement.schedule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-schedule.html) property. It returns an [IVisualElementScheduledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.html) interface that provides methods to schedule the action.   
  
For example, you can delay running of the action with the [IVisualElementScheduledItem.StartingIn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.StartingIn.html) method. You can also specify a condition to unschedule the action with the [IVisualElementScheduledItem.Until](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.Until.html) method.   
  
To repeat the action at a specified interval, use the [IVisualElementScheduledItem.Every](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.Every.html) method. To remove the scheduler, use the [IVisualElementScheduledItem.Pause](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.Pause.html) method.   
  
The scheduler is active only when the VisualElement is attached to a panel. Detaching the VisualElement from the panel pauses the scheduler, and reattaching it resumes the scheduler.   
  
Additional resources: [VisualElement.schedule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-schedule.html), [VisualElement.panel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-panel.html), [IVisualElementScheduledItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.html)   
  

```
 // This example uses the scheduler to animate the title logo by changing its background image 
 // to the next frame every 200 milliseconds.
 int m_CurrentTitleLogoFrame = 0;
 public List<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)> m_TitleLogoFrames = new List<Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)>();
 // Animate title logo.
 var titleLogo = root.Q("menu-title-image");
 titleLogo?.schedule.Execute(() =>
 {
     if (m_TitleLogoFrames.Count == 0)
         return;  
  
         m_CurrentTitleLogoFrame = (m_CurrentTitleLogoFrame + 1) % m_TitleLogoFrames.Count;
         var frame = m_TitleLogoFrames[m_CurrentTitleLogoFrame];
         titleLogo.style.backgroundImage = frame;
 }).Every(200);

```

```
 // This example uses the scheduler to animate the scaling of a VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).
 IVisualElementScheduledItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduledItem.html) m_AnimationScheduler = null;
 
 public void DoScale()
 {
 // Scale[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Scale.html) the VisualElement[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).
 }  
 
 m_AnimationScheduler = this.schedule.Execute(DoScale).Every(1).StartingIn(0);
 
 // Stop the animation
 m_AnimationScheduler.Pause();

```

### Public Methods
Method | Description  
---|---  
[Execute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IVisualElementScheduler.Execute.html) |  Schedule this action to be executed later.   
* * *
