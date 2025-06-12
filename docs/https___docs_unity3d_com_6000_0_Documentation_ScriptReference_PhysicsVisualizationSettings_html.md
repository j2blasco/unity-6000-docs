* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.html

# PhysicsVisualizationSettings
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
This class contains the settings controlling the Physics Debug Visualization.
Additional resources: [PhysicsDebugWindow](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsDebugWindow.html).
### Static Properties
Property | Description  
---|---  
[articulationBodyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-articulationBodyColor.html) | Color for Articulation Bodies.  
[baseAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-baseAlpha.html) | Alpha amount used for transparency blending.  
[centerOfMassUseScreenSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-centerOfMassUseScreenSize.html) | Whether or not the center of mass visualization should be constant screen space size.  
[colorVariance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-colorVariance.html) | Used to disinguish neighboring Colliders.  
[contactColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-contactColor.html) | Contact arrow color.  
[contactImpulseColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-contactImpulseColor.html) |  ContactPoint.impulse arrow color.  
[contactSeparationColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-contactSeparationColor.html) | Contact point separation color.  
[devOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-devOptions.html) | Shows extra options used to develop and debug the physics visualization.  
[dirtyCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-dirtyCount.html) | Dirty marker used for refreshing the GUI.  
[enableMouseSelect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-enableMouseSelect.html) | Enables the mouse-over highlighting and mouse selection modes.  
[forceOverdraw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-forceOverdraw.html) | Forcing the drawing of Colliders on top of any other geometry, regardless of depth.  
[inertiaTensorScale](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-inertiaTensorScale.html) | The scale by which the inertia tensor lines are multiplied.  
[kinematicColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-kinematicColor.html) | Color for kinematic Rigidbodies.  
[maxNumberOfQueries](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-maxNumberOfQueries.html) | The maximum number of queries that the PhysicsDebugWindow will visualize at one given time.  
[queryColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-queryColor.html) | Color that the Physics Debugger uses for query visualization.  
[rigidbodyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-rigidbodyColor.html) | Color for Rigidbodies, primarily active ones.  
[showAllContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-showAllContacts.html) | Whether the PhysicsDebugWindow visualizes all contacts.  
[showCollisionGeometry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-showCollisionGeometry.html) | Should the PhysicsDebugWindow display the collision geometry.  
[showContactImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-showContactImpulse.html) | Whether the PhysicsDebugWindow shows ContactPoint.impulse.  
[showContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-showContacts.html) | Whether the PhysicsDebugWindow shows contacts.  
[showContactSeparation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-showContactSeparation.html) | Whether the PhysicsDebugWindow shows contact separation.  
[sleepingBodyColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-sleepingBodyColor.html) | Color for Rigidbodies that are controlled by the physics simulator, but are not currently being simulated.  
[staticColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-staticColor.html) | Color for Colliders that do not have a Rigidbody component.  
[terrainTilesMax](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-terrainTilesMax.html) | Maximum number of mesh tiles available to draw all Terrain Colliders.  
[triggerColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-triggerColor.html) | Color for Colliders that are Triggers.  
[useContactFiltering](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-useContactFiltering.html) | Whether PhysicsDebugWindow takes the PhysicsVisualizationSettings filtering settings into account when visualizing contacts.  
[useSceneCam](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-useSceneCam.html) | Controls whether the SceneView or the GameView camera is used. Not shown in the UI.  
[useVariedContactColors](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-useVariedContactColors.html) | Whether varied colors are used for PhysicsDebugWindow contact visualization.  
[viewDistance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings-viewDistance.html) | Colliders within this distance will be displayed.  
### Static Methods
Method | Description  
---|---  
[ClearMouseHighlight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.ClearMouseHighlight.html) | Clears the highlighted Collider.  
[DeinitDebugDraw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.DeinitDebugDraw.html) | Deinitializes the physics debug visualization system and tracking of changes Colliders.  
[GetQueryFilterState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetQueryFilterState.html) | Gets the query filtering state of PhysicsVisualizationSettings  
[GetShowArticulationBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowArticulationBodies.html) | Should Articulation Bodies be shown by the Physics Visualizer.  
[GetShowBoxColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowBoxColliders.html) | Should BoxColliders be shown.  
[GetShowCapsuleColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowCapsuleColliders.html) | Should CapsuleColliders be shown.  
[GetShowCollisionLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowCollisionLayer.html) | Should the given layer be considered by the display filter.  
[GetShowCollisionLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowCollisionLayerMask.html) | Should the mask representing the layers be considered by the display filter.  
[GetShowKinematicBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowKinematicBodies.html) | Should the kinematic Rigidbodies be considered by the display filter.  
[GetShowMeshColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowMeshColliders.html) | Should MeshColliders be shown.  
[GetShowPhysicsSceneMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowPhysicsSceneMask.html) | Return a mask representing scenes that are enabled by display filter  
[GetShowRigidbodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowRigidbodies.html) | Should any Rigidbodies be considered by the display filter.  
[GetShowSleepingBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowSleepingBodies.html) | Should the sleeping Rigidbodies be considered by the display filter.  
[GetShowSphereColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowSphereColliders.html) | Should SphereColliders be shown.  
[GetShowStaticColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowStaticColliders.html) | Should the Colliders without a Rigidbody component be considered by the display filter.  
[GetShowTerrainColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowTerrainColliders.html) | Should TerrainColliders be shown.  
[GetShowTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowTriggers.html) | Should the triggers be considered by the display filter.  
[GetShowUnitySceneMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.GetShowUnitySceneMask.html) | Returns a mask that represents Unity scenes that are enabled by the display filter.  
[HasMouseHighlight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.HasMouseHighlight.html) | Returns true if there currently is any kind of physics object highlighted.  
[InitDebugDraw](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.InitDebugDraw.html) | Initializes the physics debug visualization system. The system must be initialized for any physics objects to be visualized. It is normally initialized by the PhysicsDebugWindow.  
[Reset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.Reset.html) | Resets the visualization options to their default state.  
[SetQueryFilterState](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetQueryFilterState.html) | Sets the query filtering state of PhysicsVisualizationSettings  
[SetShowArticulationBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowArticulationBodies.html) | Should Articulation Bodies be shown by the Physics Visualizer.  
[SetShowBoxColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowBoxColliders.html) | Should BoxColliders be shown.  
[SetShowCapsuleColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowCapsuleColliders.html) | Should CapsuleColliders be shown.  
[SetShowCollisionLayer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowCollisionLayer.html) | Should the given layer be considered by the display filter.  
[SetShowCollisionLayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowCollisionLayerMask.html) | Should the mask representing the layers be considered by the display filter.  
[SetShowForAllFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowForAllFilters.html) | Enables or disables all filtering items.  
[SetShowKinematicBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowKinematicBodies.html) | Should the kinematic Rigidbodies be considered by the display filter.  
[SetShowMeshColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowMeshColliders.html) | Should MeshColliders be shown.  
[SetShowPhysicsSceneMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowPhysicsSceneMask.html) | Should the scene mask be considered by the display filter.  
[SetShowRigidbodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowRigidbodies.html) | Should any Rigidbodies be considered by the display filter.  
[SetShowSleepingBodies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowSleepingBodies.html) | Should sleeping Rigidbodies and Articulation Bodies be considered by the display filter.  
[SetShowSphereColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowSphereColliders.html) | Should SphereColliders be shown.  
[SetShowStaticColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowStaticColliders.html) | Should the Colliders without a Rigidbody component be considered by the display filter.  
[SetShowTerrainColliders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowTerrainColliders.html) | Should TerrainColliders be shown.  
[SetShowTriggers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowTriggers.html) | Should the triggers be considered by the display filter.  
[SetShowUnitySceneMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.SetShowUnitySceneMask.html) | Sets the Unity scene mask that should be considered by the filter.  
[UpdateMouseHighlight](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsVisualizationSettings.UpdateMouseHighlight.html) | Updates the mouse-over highlight at the given mouse position in screen space.  
* * *
