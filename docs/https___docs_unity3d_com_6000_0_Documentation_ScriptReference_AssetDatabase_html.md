* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.html

# AssetDatabase
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
An Interface for accessing assets and performing operations on assets.
### Static Properties
Property | Description  
---|---  
[ActiveRefreshImportMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ActiveRefreshImportMode.html) | Gets the refresh import mode currently in use by the asset database.  
[DesiredWorkerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DesiredWorkerCount.html) | The desired number of processes to use when importing assets, during an asset database refresh.  
[GlobalArtifactDependencyVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GlobalArtifactDependencyVersion.html) | Changes during Refresh if anything has changed that can invalidate any artifact.  
[GlobalArtifactProcessedVersion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GlobalArtifactProcessedVersion.html) | Changes whenever a new artifact is added to the artifact database.  
[onImportPackageItemsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-onImportPackageItemsCompleted.html) | Callback raised whenever a package import successfully completes that lists the items selected to be imported.  
### Static Methods
Method | Description  
---|---  
[AddObjectToAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AddObjectToAsset.html) | Adds objectToAdd to an existing asset at path.  
[AllowAutoRefresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AllowAutoRefresh.html) | Decrements an internal counter which Unity uses to determine whether to allow automatic AssetDatabase refreshing behavior.  
[AssetPathExists](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathExists.html) | Check whether an asset exists at the given path in the database.  
[AssetPathToGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.AssetPathToGUID.html) | Get the GUID for the asset at path.  
[CanConnectToCacheServer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanConnectToCacheServer.html) | Checks the availability of the Cache Server.  
[CanOpenAssetInEditor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanOpenAssetInEditor.html) | Checks if Unity can open an asset in the Editor.  
[CanOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CanOpenForEdit.html) | Query whether an Asset file can be opened for editing in version control and is not exclusively locked by another user or otherwise unavailable.  
[ClearImporterOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearImporterOverride.html) | Clears the importer override for the asset.  
[ClearLabels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ClearLabels.html) | Removes all labels attached to an asset.  
[CloseCacheServerConnection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CloseCacheServerConnection.html) | Closes an active cache server connection. If no connection is active, then it does nothing.  
[Contains](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Contains.html) | Is object an asset?  
[CopyAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAsset.html) | Duplicates the asset at path and stores it at newPath.  
[CopyAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CopyAssets.html) | Duplicates assets in paths and stores them in newPaths.  
[CreateAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateAsset.html) | Creates a new native Unity asset.  
[CreateFolder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.CreateFolder.html) | Creates a new folder, in the specified parent folder.The parent folder string must start with the "Assets" folder, and all folders within the parent folder string must already exist. For example, when specifying "Assets/ParentFolder1/Parentfolder2/", the new folder will be created in "ParentFolder2" only if ParentFolder1 and ParentFolder2 already exist.  
[DeleteAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DeleteAsset.html) | Deletes the specified asset or folder.  
[DeleteAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DeleteAssets.html) | Lets you delete multiple assets or folders at once with performance benefits under version control.  
[DisallowAutoRefresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.DisallowAutoRefresh.html) | Increments an internal counter which Unity uses to determine whether to allow automatic AssetDatabase refreshing behavior.  
[ExportPackage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ExportPackage.html) | Exports the assets identified by assetPathNames to a unitypackage file in fileName.  
[ExtractAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ExtractAsset.html) | Creates an external Asset from an object (such as a Material) by extracting it from within an imported asset (such as an FBX file).  
[FindAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.FindAssets.html) | Search the asset database using the search filter string.  
[ForceReserializeAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ForceReserializeAssets.html) | Forcibly load and re-serialize the given assets, flushing any outstanding data changes to disk.  
[ForceToDesiredWorkerCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ForceToDesiredWorkerCount.html) | Forces the Editor to use the desired amount of worker processes. Unity will either spawn new worker processes or shut down idle worker processes to reach the desired number.  
[GenerateUniqueAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GenerateUniqueAssetPath.html) | Creates a new unique path for an asset.  
[GetAllAssetBundleNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAllAssetBundleNames.html) | Return all the AssetBundle names in the asset database.  
[GetAssetBundleDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetBundleDependencies.html) | Given an assetBundleName, returns the list of AssetBundles that it depends on.  
[GetAssetDependencyHash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetDependencyHash.html) | Returns the hash of all the dependencies of an asset.  
[GetAssetOrScenePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetOrScenePath.html) | Returns the path name relative to the project folder where the asset is stored.  
[GetAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPath.html) | Returns the path name relative to the project folder where the asset is stored.  
[GetAssetPathFromTextMetaFilePath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathFromTextMetaFilePath.html) | Gets the path to the asset file associated with a text .meta file.  
[GetAssetPathsFromAssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundle.html) | Returns an array containing the paths of all assets marked with the specified Asset Bundle name.  
[GetAssetPathsFromAssetBundleAndAssetName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundleAndAssetName.html) | Get the Asset paths for all Assets tagged with assetBundleName and named assetName.  
[GetAvailableImporters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetAvailableImporters.html) | Gets the importer types associated with a given Asset path.  
[GetCachedIcon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCachedIcon.html) | Retrieves an icon for the asset at the given asset path.  
[GetCacheServerAddress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerAddress.html) | Gets the IP address of the Cache Server in Editor Settings.  
[GetCacheServerEnableDownload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerEnableDownload.html) | Gets the Cache Server Download option from Editor Settings.  
[GetCacheServerEnableUpload](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerEnableUpload.html) | Gets the Cache Server Upload option from Editor Settings.  
[GetCacheServerNamespacePrefix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerNamespacePrefix.html) | Gets the Cache Server Namespace prefix set in Editor Settings.  
[GetCacheServerPort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCacheServerPort.html) | Gets the Port number of the Cache Server in Editor Settings.  
[GetCurrentCacheServerIp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetCurrentCacheServerIp.html) | Gets the IP address of the Cache Server currently in use by the Editor.  
[GetDefaultImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetDefaultImporter.html) | Returns the Default Importer associated with the asset located at the supplied path. When no Importer override is set, then the default importer is used. Additional resources: AssetDatabase.GetImporterOverride, AssetDatabase.ClearImporterOverride.  
[GetDependencies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetDependencies.html) | Returns an array of all the assets that are dependencies of the asset at the specified pathName.Note: GetDependencies() gets the Assets that are referenced by other Assets. For example, a Scene could contain many GameObjects with a Material attached to them. In this case, GetDependencies() will return the path to the Material Assets, but not the GameObjects as those are not Assets on your disk.  
[GetImplicitAssetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImplicitAssetBundleName.html) | Returns the name of the AssetBundle that a given asset belongs to.  
[GetImplicitAssetBundleVariantName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImplicitAssetBundleVariantName.html) | Returns the name of the AssetBundle Variant that a given asset belongs to.  
[GetImporterOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterOverride.html) | Returns the type of the override importer.  
[GetImporterType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterType.html) | Returns the type of importer associated with an asset without loading the asset.  
[GetImporterTypes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetImporterTypes.html) | Returns the types of importers associated with the specified array of assets, without loading those assets.  
[GetLabels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetLabels.html) | Returns all labels attached to a given asset.  
[GetMainAssetTypeAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeAtPath.html) | Returns the type of the main asset object at assetPath.  
[GetMainAssetTypeFromGUID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetMainAssetTypeFromGUID.html) | Returns the type of the main asset object with guid.  
[GetScriptableObjectsWithMissingScriptCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetScriptableObjectsWithMissingScriptCount.html) | Checks how many unloadable ScriptableObject instances are present in the specified asset.  
[GetSubFolders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetSubFolders.html) | Given a path to a directory in the Assets folder, relative to the project folder, this method will return an array of all its subdirectories.  
[GetTextMetaFilePathFromAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetTextMetaFilePathFromAssetPath.html) | Gets the path to the text .meta file associated with an asset.  
[GetTypeFromPathAndFileID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetTypeFromPathAndFileID.html) | Gets an object's type from an Asset path and a local file identifier.  
[GetUnusedAssetBundleNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GetUnusedAssetBundleNames.html) | Return all the unused assetBundle names in the asset database.  
[GUIDFromAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDFromAssetPath.html) | Get the GUID for the asset at path.  
[GUIDToAssetPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.GUIDToAssetPath.html) | Gets the corresponding asset path for the supplied GUID, or an empty string if the GUID can't be found.  
[ImportAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportAsset.html) | Import asset at path.  
[ImportPackage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportPackage.html) | Imports package at packagePath into the current project.  
[InstanceIDsToGUIDs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.InstanceIDsToGUIDs.html) | Sets a NativeArray of UnityEditor.GUIDs for every valid Instance ID that is an asset.  
[IsCacheServerEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsCacheServerEnabled.html) | Checks whether the Cache Server is enabled in Project Settings.  
[IsConnectedToCacheServer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsConnectedToCacheServer.html) | Checks connection status of the Cache Server.  
[IsDirectoryMonitoringEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsDirectoryMonitoringEnabled.html) | Reports whether Directory Monitoring is enabled.  
[IsForeignAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsForeignAsset.html) | Determines whether the Asset is a foreign Asset.  
[IsMainAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAsset.html) | Is asset a main asset in the project window?  
[IsMainAssetAtPathLoaded](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMainAssetAtPathLoaded.html) | Returns true if the main asset object at assetPath is loaded in memory.  
[IsMetaFileOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsMetaFileOpenForEdit.html) | Query whether an asset's metadata (.meta) file is open for edit in version control.  
[IsNativeAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsNativeAsset.html) | Determines whether the Asset is a native Asset.  
[IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html) | Query whether an Asset file is open for editing in version control.  
[IsSubAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsSubAsset.html) | Does the asset form part of another asset?  
[IsValidFolder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsValidFolder.html) | Given a path to a folder, returns true if it exists, false otherwise.  
[LoadAllAssetRepresentationsAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetRepresentationsAtPath.html) | Returns all sub Assets at assetPath.  
[LoadAllAssetsAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAllAssetsAtPath.html) | Returns an array of all Assets at assetPath.  
[LoadAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadAssetAtPath.html) | Returns the first asset object of type type at given path assetPath.  
[LoadMainAssetAtPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadMainAssetAtPath.html) | Returns the main asset object at assetPath.The "main" Asset is the Asset at the root of a hierarchy (such as a Maya file which may contain multiples meshes and GameObjects).  
[LoadObjectAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.LoadObjectAsync.html) | Loads a specific Object and its dependencies from an Asset file asynchronously.  
[MakeEditable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MakeEditable.html) | Makes a file open for editing in version control.  
[MoveAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAsset.html) | Move an asset file (or folder) from one folder to another.  
[MoveAssetsToTrash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetsToTrash.html) | Lets you move multiple assets or folders to trash at once with performance benefits under version control.  
[MoveAssetToTrash](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MoveAssetToTrash.html) | Moves the specified asset or folder to the OS trash.  
[OpenAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.OpenAsset.html) | Opens the asset with associated application.  
[Refresh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.Refresh.html) | Import any changed assets.  
[RefreshSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RefreshSettings.html) | Apply pending Editor Settings changes to the Asset pipeline.  
[RegisterCustomDependency](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RegisterCustomDependency.html) | Allows you to register a custom dependency that Assets can be dependent on. If you register a custom dependency, and specify that an Asset is dependent on it, then the Asset will get re-imported if the custom dependency changes.  
[ReleaseCachedFileHandles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ReleaseCachedFileHandles.html) | Calling this function will release file handles internally cached by Unity. This allows modifying asset or meta files safely thus avoiding potential file sharing IO errors.  
[RemoveAssetBundleName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveAssetBundleName.html) | Remove the assetBundle name from the asset database. The forceRemove flag is used to indicate if you want to remove it even it's in use.  
[RemoveObjectFromAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveObjectFromAsset.html) | Removes object from its asset (Additional resources: AssetDatabase.AddObjectToAsset).  
[RemoveScriptableObjectsWithMissingScript](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveScriptableObjectsWithMissingScript.html) | Removes any ScriptableObject instances from the given asset file which cannot be loaded because their scripts could not be found.  
[RemoveUnusedAssetBundleNames](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RemoveUnusedAssetBundleNames.html) | Remove all the unused assetBundle names in the asset database.  
[RenameAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.RenameAsset.html) | Rename an asset file.  
[ResetCacheServerReconnectTimer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ResetCacheServerReconnectTimer.html) | Resets the internal cache server connection reconnect timer values. The default delay timer value is 1 second, and the max delay value is 5 minutes. Everytime a connection attempt fails it will double the delay timer value, until a maximum time of the max value.  
[SaveAssetIfDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssetIfDirty.html) | Writes all unsaved changes to the specified asset to disk.  
[SaveAssets](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SaveAssets.html) | Writes all unsaved asset changes to disk.  
[SetImporterOverride](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetImporterOverride.html) | Sets a specific importer to use for the asset.  
[SetLabels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetLabels.html) | Replaces that list of labels on an asset.  
[SetMainObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.SetMainObject.html) | Specifies which object in the asset file should become the main object after the next import.  
[StartAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StartAssetEditing.html) | Pauses automatic asset import, allowing you to group several asset imports together into one larger import.  
[StopAssetEditing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.StopAssetEditing.html) | Ends the Asset Database's temporary paused state, allowing it to resume normal automatic imports.  
[TryGetAssetFolderInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetAssetFolderInfo.html) | Get AssetDatabase specific information about a folder.  
[TryGetGUIDAndLocalFileIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.TryGetGUIDAndLocalFileIdentifier.html) | Get the GUID and local file id from an object instance id.  
[UnregisterCustomDependencyPrefixFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.UnregisterCustomDependencyPrefixFilter.html) | Removes custom dependencies that match the prefixFilter.  
[ValidateMoveAsset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ValidateMoveAsset.html) | Checks if an asset file can be moved from one folder to another. (Without actually moving the file).  
[WriteImportSettingsIfDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.WriteImportSettingsIfDirty.html) | Writes the import settings to disk.  
### Events
Event | Description  
---|---  
[cacheServerConnectionChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-cacheServerConnectionChanged.html) | Unity raises this event when Cache Server connection is changed.  
[importPackageCancelled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageCancelled.html) | Callback raised whenever a package import is cancelled by the user.  
[importPackageCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageCompleted.html) | Callback raised whenever a package import successfully completes.  
[importPackageFailed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageFailed.html) | Callback raised whenever a package import failed.  
[importPackageStarted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase-importPackageStarted.html) | Callback raised whenever a package import starts.  
### Delegates
Delegate | Description  
---|---  
[ImportPackageCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportPackageCallback.html) | Delegate to be called from AssetDatabase.ImportPackage callbacks. packageName is the name of the package that raised the callback.  
[ImportPackageFailedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.ImportPackageFailedCallback.html) | Delegate to be called from AssetDatabase.ImportPackage callbacks. packageName is the name of the package that raised the callback. errorMessage is the reason for the failure.  
* * *
