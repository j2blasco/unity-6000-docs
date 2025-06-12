* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.html

# Tilemap
class in UnityEngine.Tilemaps
/
Inherits from:[GridLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.html)
/
Implemented in:[UnityEngine.TilemapModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.TilemapModule.html)
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
The Tilemap stores [Sprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Sprite.html)s in a layout marked by a [Grid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Grid.html) component.
### Properties
Property | Description  
---|---  
[animationFrameRate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-animationFrameRate.html) | The frame rate for all Tile animations in the Tilemap.  
[cellBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-cellBounds.html) | Returns the boundaries of the Tilemap in cell size.  
[color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-color.html) | The color of the Tilemap layer.  
[editorPreviewOrigin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-editorPreviewOrigin.html) | The origin of the Tilemap in cell position inclusive of editor preview Tiles.  
[editorPreviewSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-editorPreviewSize.html) | The size of the Tilemap in cells inclusive of editor preview Tiles.  
[layoutGrid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-layoutGrid.html) | Gets the Grid associated with this Tilemap.  
[localBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-localBounds.html) | Returns the boundaries of the Tilemap in local space size.  
[orientation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-orientation.html) | Orientation of the Tiles in the Tilemap.  
[orientationMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-orientationMatrix.html) | Orientation Matrix of the orientation of the Tiles in the Tilemap.  
[origin](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-origin.html) | The origin of the Tilemap in cell position.  
[size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-size.html) | The size of the Tilemap in cells.  
[tileAnchor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-tileAnchor.html) | Gets the anchor point of Tiles in the Tilemap.  
### Public Methods
Method | Description  
---|---  
[AddTileAnimationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.AddTileAnimationFlags.html) | Adds the TileAnimationFlags onto the Tile at the given position.  
[AddTileFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.AddTileFlags.html) | Adds the TileFlags onto the Tile at the given position.  
[BoxFill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.BoxFill.html) | Does a box fill with the given Tile on the Tilemap. Starts from given coordinates and fills the limits from start to end (inclusive).  
[ClearAllEditorPreviewTiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.ClearAllEditorPreviewTiles.html) | Clears all editor preview Tiles that are placed in the Tilemap.  
[ClearAllTiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.ClearAllTiles.html) | Clears all Tiles that are placed in the Tilemap.  
[CompressBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.CompressBounds.html) | Compresses the origin and size of the Tilemap to bounds where Tiles exist.  
[ContainsTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.ContainsTile.html) | Returns true if the Tilemap contains the given Tile. Returns false if not.  
[DeleteCells](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.DeleteCells.html) | Removes cells from within the Tilemap's bounds.  
[EditorPreviewBoxFill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.EditorPreviewBoxFill.html) | Does an editor preview of a box fill with the given Tile on the Tilemap. Starts from given coordinates and fills the limits from start to end (inclusive).  
[EditorPreviewFloodFill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.EditorPreviewFloodFill.html) | Does an editor preview of a flood fill with the given Tile to place. on the Tilemap starting from the given coordinates.  
[FloodFill](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.FloodFill.html) | Does a flood fill with the given Tile to place. on the Tilemap starting from the given coordinates.  
[GetAnimationFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetAnimationFrame.html) | Retrieves the current animation frame for a Tile at the given position.  
[GetAnimationFrameCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetAnimationFrameCount.html) | Retrieves the number of animation frames for a Tile at the given position.  
[GetAnimationTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetAnimationTime.html) | Retrieves the current running animation time for a Tile at the given position.  
[GetCellCenterLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetCellCenterLocal.html) | Gets the logical center coordinate of a Grid cell in local space. The logical center for a cell of the Tilemap is defined by the Tile Anchor of the Tilemap.  
[GetCellCenterWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetCellCenterWorld.html) | Gets the logical center coordinate of a Grid cell in world space. The logical center for a cell of the Tilemap is defined by the Tile Anchor of the Tilemap.  
[GetColliderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetColliderType.html) | Gets the Collider type of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetColor.html) | Gets the Color of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetEditorPreviewColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetEditorPreviewColor.html) | Gets the Color of an editor preview Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetEditorPreviewSprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetEditorPreviewSprite.html) | Gets the Sprite used in an editor preview Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetEditorPreviewTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetEditorPreviewTile.html) | Gets the editor preview Tile at the given XYZ coordinates of a cell in the Tilemap.  
[GetEditorPreviewTileFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetEditorPreviewTileFlags.html) | Gets the TileFlags of the editor preview Tile at the given position.  
[GetEditorPreviewTransformMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetEditorPreviewTransformMatrix.html) | Gets the transform matrix of an editor preview Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetInstantiatedObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetInstantiatedObject.html) | Gets the GameObject instantiated by a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetObjectToInstantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetObjectToInstantiate.html) | Gets the GameObject which will be instantiated by a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetSprite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetSprite.html) | Gets the Sprite used in a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTile.html) | Gets the Tile at the given XYZ coordinates of a cell in the Tilemap.  
[GetTileAnimationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTileAnimationFlags.html) | Gets the TileAnimationFlags of the Tile at the given position.  
[GetTileFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTileFlags.html) | Gets the TileFlags of the Tile at the given position.  
[GetTilesBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTilesBlock.html) | Retrieves an array of Tiles with the given bounds.  
[GetTilesBlockNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTilesBlockNonAlloc.html) | Retrieves an array of Tiles with the given bounds.  
[GetTilesRangeCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTilesRangeCount.html) | Retrieves the number of Tiles within the given range, inclusive of the Cells at both the starting position and the ending positions. This method begins at the given starting position and iterates through all available Z Positions, then iterates through the X and Y positions until it reaches the ending position.  
[GetTilesRangeNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTilesRangeNonAlloc.html) | Retrieves an array of Tiles within the given range, inclusive of the Cells at both the starting position and the ending positions. This method begins at the given starting position and iterates through all available Z Positions, then iterates through the X and Y positions until it reaches the ending position.  
[GetTransformMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetTransformMatrix.html) | Gets the transform matrix of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[GetUsedSpritesCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetUsedSpritesCount.html) | Gets the total number of different Sprites used in the Tilemap.  
[GetUsedSpritesNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetUsedSpritesNonAlloc.html) | Fills the given array with the total number of different Sprites used in the Tilemap and returns the number of Sprites filled.  
[GetUsedTilesCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetUsedTilesCount.html) | Gets the total number of different Tiles used in the Tilemap.  
[GetUsedTilesNonAlloc](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.GetUsedTilesNonAlloc.html) | Fills the given array with the total number of different Tiles used in the Tilemap and returns the number of Tiles filled.  
[HasEditorPreviewTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.HasEditorPreviewTile.html) | Returns whether there is an editor preview Tile at the position.  
[HasTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.HasTile.html) | Returns whether there is a Tile at the position.  
[InsertCells](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.InsertCells.html) | Inserts cells into the Tilemap.  
[RefreshAllTiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.RefreshAllTiles.html) | Refreshes all Tiles in the Tilemap. The Tilemap will retrieve the rendering data, animation data and other data for all tiles and update all relevant components.  
[RefreshTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.RefreshTile.html) | Refreshes a Tile at the given XYZ coordinates of a cell in the Tilemap.  
[RemoveTileAnimationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.RemoveTileAnimationFlags.html) | Removes the TileAnimationFlags from the Tile at the given position.  
[RemoveTileFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.RemoveTileFlags.html) | Removes the TileFlags from the Tile at the given position.  
[ResizeBounds](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.ResizeBounds.html) | Resizes Tiles in the Tilemap to bounds defined by origin and size.  
[SetAnimationFrame](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetAnimationFrame.html) | Sets the current animation frame for a Tile at the given position.  
[SetAnimationTime](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetAnimationTime.html) | Sets the running animation time for a Tile at the given position.  
[SetColliderType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetColliderType.html) | Sets the Collider type of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[SetColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetColor.html) | Sets the color of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[SetEditorPreviewColor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetEditorPreviewColor.html) | Sets the color of an editor preview Tile given the XYZ coordinates of a cell in the Tilemap.  
[SetEditorPreviewTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetEditorPreviewTile.html) | Sets an editor preview Tile given the XYZ coordinates of a cell in the Tilemap.  
[SetEditorPreviewTransformMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetEditorPreviewTransformMatrix.html) | Sets the transform matrix of an editor preview Tile given the XYZ coordinates of a cell in the Tilemap.  
[SetTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetTile.html) | Sets a Tile at the given XYZ coordinates of a cell in the Tilemap.  
[SetTileAnimationFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetTileAnimationFlags.html) | Sets the TileAnimationFlags onto the Tile at the given position.  
[SetTileFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetTileFlags.html) | Sets the TileFlags onto the Tile at the given position.  
[SetTiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetTiles.html) | Sets an array of Tiles at the given XYZ coordinates of the corresponding cells in the Tilemap.  
[SetTilesBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetTilesBlock.html) | Fills bounds with array of Tiles.  
[SetTransformMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SetTransformMatrix.html) | Sets the transform matrix of a Tile given the XYZ coordinates of a cell in the Tilemap.  
[SwapTile](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap.SwapTile.html) | Swaps all existing Tiles of changeTile to newTile and refreshes all the swapped Tiles.  
### Events
Event | Description  
---|---  
[loopEndedForTileAnimation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-loopEndedForTileAnimation.html) | Callback when Tiles on a Tilemap have reached the end of their loop for their Tile Animation.  
[tilemapPositionsChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-tilemapPositionsChanged.html) | Callback when Tiles on a Tilemap have changed.  
[tilemapTileChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Tilemaps.Tilemap-tilemapTileChanged.html) | Callback when Tiles on a Tilemap have changed.  
### Inherited Members
### Properties
Property | Description  
---|---  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-enabled.html) | Enabled Behaviours are Updated, disabled Behaviours are not.  
[isActiveAndEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Behaviour-isActiveAndEnabled.html) | Reports whether a GameObject and its associated Behaviour is active and enabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-gameObject.html) | The game object this component is attached to. A component is always attached to a game object.  
[tag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-tag.html) | The tag of this game object.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component-transform.html) | The Transform attached to this GameObject.  
[cellGap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout-cellGap.html) | The size of the gap between each cell in the layout.  
[cellLayout](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout-cellLayout.html) | The layout of the cells.  
[cellSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout-cellSize.html) | The size of each cell in the layout.  
[cellSwizzle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout-cellSwizzle.html) | The cell swizzle for the layout.  
[hideFlags](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-hideFlags.html) | Should the object be hidden, saved with the Scene or modifiable by the user?  
[name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-name.html) | The name of the object.  
### Public Methods
Method | Description  
---|---  
[BroadcastMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.BroadcastMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object or any of its children.  
[CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.CompareTag.html) | Checks the GameObject's tag against the defined tag.  
[GetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponent.html) | Gets a reference to a component of type T on the same GameObject as the component specified.  
[GetComponentInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInChildren.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any child of the GameObject.  
[GetComponentIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentIndex.html) | Gets the index of the component on its parent GameObject.  
[GetComponentInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentInParent.html) | Gets a reference to a component of type T on the same GameObject as the component specified, or any parent of the GameObject.  
[GetComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponents.html) | Gets references to all components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInChildren.html) | Gets references to all components of type T on the same GameObject as the component specified, and any child of the GameObject.  
[GetComponentsInParent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.GetComponentsInParent.html) | Gets references to all components of type T on the same GameObject as the component specified, and any parent of the GameObject.  
[SendMessage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessage.html) | Calls the method named methodName on every MonoBehaviour in this game object.  
[SendMessageUpwards](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.SendMessageUpwards.html) | Calls the method named methodName on every MonoBehaviour in this game object and on every ancestor of the behaviour.  
[TryGetComponent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Component.TryGetComponent.html) | Gets the component of the specified type, if it exists.  
[CellToLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.CellToLocal.html) | Converts a cell position to local position space.  
[CellToLocalInterpolated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.CellToLocalInterpolated.html) | Converts an interpolated cell position in floats to local position space.  
[CellToWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.CellToWorld.html) | Converts a cell position to world position space.  
[GetBoundsLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.GetBoundsLocal.html) | Returns the local bounds for a cell at the location.  
[GetLayoutCellCenter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.GetLayoutCellCenter.html) | Get the default center coordinate of a cell for the set layout of the Grid.  
[LocalToCell](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.LocalToCell.html) | Converts a local position to cell position.  
[LocalToCellInterpolated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.LocalToCellInterpolated.html) | Converts a local position to cell position.  
[LocalToWorld](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.LocalToWorld.html) | Converts a local position to world position.  
[WorldToCell](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.WorldToCell.html) | Converts a world position to cell position.  
[WorldToLocal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GridLayout.WorldToLocal.html) | Converts a world position to local position.  
[GetInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.GetInstanceID.html) | Gets the instance ID of the object.  
[ToString](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.ToString.html) | Returns the name of the object.  
### Static Methods
Method | Description  
---|---  
[Destroy](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Destroy.html) | Removes a GameObject, component or asset.  
[DestroyImmediate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DestroyImmediate.html) | Destroys the object obj immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.DontDestroyOnLoad.html) | Do not destroy the target Object when loading a new Scene.  
[FindAnyObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindAnyObjectByType.html) | Retrieves any active loaded object of Type type.  
[FindFirstObjectByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindFirstObjectByType.html) | Retrieves the first active loaded object of Type type.  
[FindObjectsByType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.FindObjectsByType.html) | Retrieves a list of all loaded objects of Type type.  
[Instantiate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.Instantiate.html) | Clones the object original and returns the clone.  
[InstantiateAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object.InstantiateAsync.html) | Captures a snapshot of the original object (that must be related to some GameObject) and returns the AsyncInstantiateOperation.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_Object.html) | Does the object exist?  
[operator !=](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_ne.html) | Compares if two objects refer to a different object.  
[operator ==](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Object-operator_eq.html) | Compares two object references to see if they refer to the same object.  
* * *
