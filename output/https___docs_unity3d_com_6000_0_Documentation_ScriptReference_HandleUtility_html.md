* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html

# HandleUtility
class in UnityEditor
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
Helper functions for Scene View style 3D GUI.
These are mainly mathematical functions that assist in converting between the 3D Scene space and the 2D GUI. The functions are used in the construction of the Unity Editor itself and so using them is a good way to make your own [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html) GUIs consistent with Unity's.
### Static Properties
Property | Description  
---|---  
[acceleration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-acceleration.html) | Get standard acceleration for dragging values (Read Only).  
[nearestControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-nearestControl.html) | The controlID of the nearest Handle to the mouse cursor.  
[niceMouseDelta](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-niceMouseDelta.html) | Get nice mouse delta to use for dragging a float value (Read Only).  
[niceMouseDeltaZoom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-niceMouseDeltaZoom.html) | Get nice mouse delta to use for zooming (Read Only).  
### Static Methods
Method | Description  
---|---  
[AddControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddControl.html) | Record a distance measurement from a handle.  
[AddDefaultControl](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.AddDefaultControl.html) | Add the ID for a default control. This will be picked if nothing else is.  
[CalcLineTranslation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.CalcLineTranslation.html) | Map a mouse drag onto a movement along a line in 3D space.  
[ClosestPointToArc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ClosestPointToArc.html) | Get the point on an arc (in 3D space) which is closest to the current mouse position.  
[ClosestPointToDisc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ClosestPointToDisc.html) | Get the point on an disc (in 3D space) which is closest to the current mouse position.  
[ClosestPointToPolyLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ClosestPointToPolyLine.html) | Get the point on a polyline (in 3D space) which is closest to the current mouse position.  
[DecodeSelectionId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DecodeSelectionId.html) | Translates a Vector4 selectionId value retrieved from GPU into a single integer picking index.  
[DistancePointBezier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistancePointBezier.html) | Calculate distance between a point and a Bezier curve.  
[DistancePointLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistancePointLine.html) | Calculate distance between a point and a line.  
[DistancePointToLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistancePointToLine.html) | Distance from a point p in 2d to a line defined by two points a and b.  
[DistancePointToLineSegment](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistancePointToLineSegment.html) | Distance from a point p in 2d to a line segment defined by two points a and b.  
[DistanceToArc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToArc.html) | Returns the distance in pixels from the mouse pointer to a 3D section of a disc.  
[DistanceToCircle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCircle.html) | Returns the distance in pixels from the mouse pointer to a camera facing circle.  
[DistanceToCone](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCone.html) | Returns the distance in pixels from the mouse pointer to a cone.  
[DistanceToCube](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCube.html) | Returns the distance in pixels from the mouse pointer to a cube.  
[DistanceToDisc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToDisc.html) | Returns the distance in pixels from the mouse pointer to a 3D disc.  
[DistanceToLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToLine.html) | Returns the distance in pixels from the mouse pointer to a line.  
[DistanceToPolyLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToPolyLine.html) | Returns the distance in pixels from the mouse pointer to a polyline.  
[DistanceToRectangle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToRectangle.html) | Returns the distance in pixels from the mouse pointer to a rectangle on screen.  
[EncodeSelectionId](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.EncodeSelectionId.html) | Translates a single integer picking index into a Vector4 selectionId value. The Vector4 selectionId is used to render the picking render textures during picking rendering.  
[FindNearestVertex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.FindNearestVertex.html) | Returns the nearest vertex to a guiPoint within a maximum radius of 50 pixels.  
[GetHandleSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetHandleSize.html) | Get world space size of a manipulator handle at given position.  
[GetOverlappingObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetOverlappingObjects.html) | Gets an ordered list of objects that would be picked under the give mouse position.  
[GetPickingIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetPickingIncludeExcludeList.html) | Gets the picking PickingIncludeExcludeList for the currently executing BatchRendererGroup.OnPerformCulling callback.  
[GetSelectionOutlineIncludeExcludeList](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GetSelectionOutlineIncludeExcludeList.html) | Gets the selection outline PickingIncludeExcludeList for the currently executing BatchRendererGroup.OnPerformCulling callback.  
[GUIPointToScreenPixelCoordinate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToScreenPixelCoordinate.html) | Converts a 2D GUI position to screen pixel coordinates.  
[GUIPointToWorldRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToWorldRay.html) | Convert 2D GUI position to a world space ray.  
[PickAllObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickAllObjects.html) | Creates a list of all GameObjects under the specified position in screen coordinates.  
[PickGameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickGameObject.html) | Pick game object closest to specified position.  
[PickRectObjects](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickRectObjects.html) | Pick GameObjects that lie within a specified screen rectangle.  
[PlaceObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PlaceObject.html) | Casts a ray against the loaded scenes and returns the nearest intersected point on a collider.  
[PointOnLineParameter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PointOnLineParameter.html) | Returns the parameter for the projection of the point on the given line.  
[PopCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PopCamera.html) | Retrieve all camera settings.  
[ProjectPointLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ProjectPointLine.html) | Project point onto a line.  
[PushCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PushCamera.html) | Store all camera settings.  
[RaySnap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RaySnap.html) | Casts ray against the Scene and reports whether an object lies in its path.  
[RegisterRenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RegisterRenderPickingCallback.html) | Registers a callback to invoke when Unity renders for picking.  
[Repaint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.Repaint.html) | Repaint the current view.  
[UnregisterRenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.UnregisterRenderPickingCallback.html) | Unregisters the callback that was previously registered for custom picking rendering.The method throws InvalidOperationException if you try to call it inside render picking callbacks.  
[WorldPointToSizedRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.WorldPointToSizedRect.html) | Calculate a rectangle to display a 2D GUI element near a projected point in 3D space.  
[WorldToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.WorldToGUIPoint.html) | Convert a world space point to a 2D GUI position.  
[WorldToGUIPointWithDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.WorldToGUIPointWithDepth.html) | Convert a world space point to a 2D GUI position.  
### Events
Event | Description  
---|---  
[getAuthoringObjectForEntity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-getAuthoringObjectForEntity.html) | The user-defined callback that Unity uses to retrieve the Unity Object associated with a DOTS Entity.  
[getEntitiesForAuthoringObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-getEntitiesForAuthoringObject.html) | The user-defined callback that Unity uses to retrieve the DOTS Entity IDs associated with a Unity Object.  
[pickGameObjectCustomPasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-pickGameObjectCustomPasses.html) | Subscribe to this event to add additional picking objects to the HandleUtility.PickGameObject method.  
[placeObjectCustomPasses](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility-placeObjectCustomPasses.html) | Subscribe to this event to handle object placement in the SceneView.  
### Delegates
Delegate | Description  
---|---  
[PickGameObjectCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PickGameObjectCallback.html) | This is the method definition for pickGameObjectCustomPasses.  
[PlaceObjectDelegate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PlaceObjectDelegate.html) | This is the method definition for placeObjectCustomPasses.  
[RenderPickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RenderPickingCallback.html) | The delegate type to use with RegisterRenderPickingCallback and UnregisterRenderPickingCallback.  
[ResolvePickingCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ResolvePickingCallback.html) | The delegate type to return from RenderPickingCallback through the RenderPickingResult.resolver member.  
[ResolvePickingWithWorldPositionCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ResolvePickingWithWorldPositionCallback.html) | The delegate type to return from RenderPickingCallback through the RenderPickingResult.resolverWithWorldPos member, with the additional world space position and depth information of where the click occurred.  
* * *
