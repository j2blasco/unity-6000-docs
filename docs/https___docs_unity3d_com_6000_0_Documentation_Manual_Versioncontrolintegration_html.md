* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Versioncontrolintegration.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Version Control](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)
  * Version control integrations


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)
Version Control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/perForceIntegration.html)
Perforce Integration
# Version control integrations
Unity has integrations with two version control systems: [Perforce](https://docs.unity3d.com/6000.0/Documentation/Manual/perForceIntegration.html)A version control system for file change management. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/perForceIntegration.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Perforce) and [Plastic SCM](https://docs.unity3d.com/6000.0/Documentation/Manual/PlasticSCMPlugin). To use the [version control](https://unity.com/products/plastic-scm/source-code-management#what-version-control) integrations in Unity, you need to have either a **Perforce** or **Plastic SCM** server set up for your Unity Project.
## Setting up version control in Unity
Open a Unity Project, go to **Edit** > **Project Settings** , and then select the **Version Control** category.
**Property** |  | **Description**  
---|---|---  
**Mode** |  | Select the version control mode.  
| **Hidden meta files** | Hide the .meta files in your operating system’s file explorer. Unity does not show .meta files in the Project view, no matter which mode you choose.  
| **Visible meta files** | Select this option to work with a version control system that Unity doesn’t support. This is the default setting. You can then manage the source Assets and metadata for those Assets with a version control system of your choice.  
| **Perforce** | Select this option if you use [Perforce](https://www.perforce.com/) as your version control system.  
**Username** |  | Enter the username associated with your Perforce account. This property is only visible when **Mode** is set to **Perforce**.  
**Password** |  | Enter the password associated with your Perforce account. This property is only visible when **Mode** is set to **Perforce**.  
**Workspace** |  | Enter your workspace. For example, `Example**Workspace**1`. This property is only visible when **Mode** is set to **Perforce**.  
**Server** |  | Enter the server your Unity Project is on. For example, localhost:1666. This property is only visible when **Mode** is set to **Perforce**.  
**Host** |  | Enter the hostname that you want your computer to impersonate. For example, workstation123.perforce.com. This property is only visible when **Mode** is set to **Perforce**.  
**Log Level** |  | Select how much version control information to receive in Unity’s console log.  
| **Verbose** | Log every operation related to version control. This option provides very detailed logging, and is useful if you want to debug your version control setup. This property is only visible when **Mode** is set to **Perforce**.  
| **Info** | Log errors, warnings, and information related to version control.  
| **Notice** | Log errors and warnings.  
| **Fatal** | Unity prints only fatal errors to the console.  
**Status** |  | Display information on the status of the connection to the version control system. If you are not connected, select **Connect** to connect to the system you have configured. This property is only visible when **Mode** is set to **Perforce**.  
**Automatic Add** |  | When this setting is enabled, automatically add your files to the version control system when you add them to the Project, either via the Editor or the folder on disk. When this setting is disabled, you need to add files manually to the version control system. This setting is enabled by default. This property is only visible when **Mode** is set to **Perforce**.  
**Work Offline** |  | Enable this setting to work offline. When this setting is enabled, you need to reconcile offline work in P4V or use the reconcile command in P4 to bring the Perforce server depot up to date with the work you did while offline. For more information, refer to [Working offline with Perforce](https://docs.unity3d.com/6000.0/Documentation/Manual/perForceIntegration.html). This property is only visible when **Mode** is set to **Perforce**.  
**Async Update** |  | Enable this setting to use asynchronous version control status queries. When enabled, Perforce updates the version control status of files without stalling the Unity Editor. Use this setting when the connection to your version control server has high latency.  
  
**Note:** Only status queries are asynchronous. Unity synchronously performs operations that change the state of files, or require up-to-date knowledge of a file status. This property is only visible when **Mode** is set to **Perforce**.  
**Show Failed Checkouts** |  | Enable this property to display a dialog when Perforce can’t perform the check out operation. This might happen if you lose connection, or if another user has exclusively checked out the Asset you want to edit. This property is only visible when **Mode** is set to **Perforce**.  
**Overwrite Failed Checkout Assets** |  | When you enable this setting, Unity saves any Assets that can not be checked out. This means Unity forces through a save to a file, even if Perforce cannot check out the file. This is enabled by default. If you disable it, Unity doesn’t force your files to save if Perforce can’t check them out. This property is only visible when **Mode** is set to **Perforce**.  
**Smart Merge** |  |  [Smart Merge](https://docs.unity3d.com/6000.0/Documentation/Manual/SmartMerge.html) makes it easier for Unity to merge files that have changes on the same line. This is useful if several users are working on the same Project at the same time. This property is only visible when **Mode** is set to **Perforce**.  
| **Off** | Disable Smart Merge.  
| **Ask** | Enable Smart Merge, but receive a notification before you merge, if a conflict happens. This is the default setting.  
| **Premerge** | Automatically use Smart Merge.  
**Version Packages Outside Project** |  | Tracks changes to packages that reside on disk outside of the Unity project’s root folder while still in the local workspace. This property is only visible when **Mode** is set to **Perforce**.  
**Overlay Icons** |  | Enable this setting to display version control status icons in the Editor. This property is only visible when **Mode** is set to **Perforce**.  
Configure the **Version Control** A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl) settings, then select the **Connect** button next to the status area to connect to the version control system. When Unity connects to the system, **Connected** displays in the status area.
To adjust your revision control tool, open **Preferences** and then select the **External Tools** section. You can choose a new tool under **Revision Control Diff/Merge**.
## Using version control in Unity
When you set the Editor up to work with your version control system, you can perform version control operations via the Editor, instead of in the version control client. To do this, right-click on the Asset in the Project view.
The version control operations vary depending on which version control you use. The following table displays what actions are available for each version control:
**Version control operation** | **Description** | **Perforce** | **Plastic SCM**  
---|---|---|---  
**Get Latest** | This updates the files on your machine to match those in the version control system. | Yes | No. To get the latest changes and update the file, you need to use the [version control window](https://docs.unity3d.com/6000.0/Documentation/Manual/Versioncontrolintegration.html#window) (**Window > Asset Management > Version Control**).  
**Submit** | Submits the current state of the files to the version control system. | Yes | Yes  
**Check Out** | Allows changes to be made to the files. | Yes | Yes  
**Check Out (Other)** | Select whether to check out both the Asset and its .meta file, or only the Asset, or only the .meta file. | Yes | No  
**Mark Add** | Adds the files into version control. | Yes | Yes  
**Revert** | Discards changes to open changed files. | Yes | Yes  
**Revert Unchanged** | Removes the checked out status from files that have previously been checked out but you haven’t modified. | Yes | Yes  
**Resolve Conflicts** | Resolves conflicts on files that have been changed by multiple users. | Yes | No. Conflicts appear in the version control menu, but you need to resolve them in the Plastic SCM GUI.  
**Lock** | Prevents other users from submitting changes to the files. | Yes | No. To lock or unlock files in Plastic SCM, you must edit a specific Plastic SCM lock file externally. For more information, see the page on [Plastic SCM Integration](https://docs.unity3d.com/6000.0/Documentation/Manual/PlasticSCMPlugin).  
**Unlock** | Releases the lock and allows anyone to submit changes. | Yes | No. To lock or unlock files in Plastic SCM, you must edit a specific Plastic SCM lock file externally. For more information, see the page on [Plastic SCM Integration](https://docs.unity3d.com/6000.0/Documentation/Manual/PlasticSCMPlugin).  
**Diff** | Compares the differences between the local files on your computer and the files on the server. You can choose to diff only the Asset file, or the Asset file and its .meta file. | Yes | Yes  
### Checking out files
In some version control systems, such as Perforce, versioned files are read-only by default, and require you to check them out before you edit them (unless you have enabled the **Work offline** setting). When you work with versioned Assets from the Editor, the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) displays a **Check Out** button that enables file editing. Additionally, **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) inspectors have a **Checkout** button that you can use to check out specific Project settings.
If you have custom Editor script code that disables parts of another custom editing tool for read-only Assets, or if you are writing to versioned files manually, use the [AssetDatabase.IsOpenForEdit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.IsOpenForEdit.html) and [AssetDatabase.MakeEditable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetDatabase.MakeEditable.html) APIs to check for file editability and to perform check out operations.
The Version Control integration also exposes [Provider.PreCheckoutCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.PreCheckoutCallback.html) and [Provider.PreSubmitCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/VersionControl.Provider.PreSubmitCallback.html) C# callbacks for custom version control operation validation logic.
Unity writes any Assets you modify or mark as modified in the Editor to the disk when it performs a **Save Project** operation. The Assets are then checked out in version control if needed. This might lead to Assets getting checked out even if no actual changes to the file happens. This most often happens when an Editor script calls [EditorUtility.SetDirty](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.SetDirty.html) on an Asset, without checking if it was modified.
**Note:** If Unity cannot commit your changes to your version control client (for example, if the server is down or if license issues occur), it stores your changes in a separate changeset.
When you save your changes to a .**scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) file, Unity automatically checks it out. If you use Plastic SCM, it also automatically checks out automatically generated Assets, such as light maps.
## Version Control window
You can use the Version Control window to view the files in your changelist. To access the window navigate to **Window > Asset Management > Version Control**.
The **Outgoing** tab lists all of the local changes that are pending a commit into version control. The **Incoming** tab lists all of the changes that need to be pulled from version control.
Right-click Assets or changelists in the window to perform operations on them. To move Assets between changelists, drag them from one changelist to the header of the target changelist.
### Icons
The Editor displays the following icons to visualize the version control status for files and Assets:
**Icon** | **Purpose**  
---|---  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_AddedLocal.png) | File added locally, and pending addition into version control.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_AddedRemote.png) | File added to version control by another user, and pending addition into version control.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_CheckOutLocal.png) | File is checked out locally.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_CheckOutRemote.png) | File is checked out by another user remotely.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_Conflicted.png) | There has been a conflict merging this file and it needs to be resolved.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_DeletedLocal.png) | File has been deleted locally, and is pending deletion in version control.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_DeletedRemote.png) | File has been deleted by another user and is pending deletion in version control.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_Local.png) | File is not yet under version control. You can use the **Mark Add** operation to add the file manually.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_LockedLocal.png) | File is locked by you and other users cannot modify it.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_LockedRemote.png) | File is locked by another user and you cannot modify it.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_OutOfSync.png) | Another user has checked in a new version of this file. Use the **Apply Incoming Changes** operation to get the latest version.  
![](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/VersionControl_P4_AsyncUpdate.png) | The server is requesting the version control status of this file, or is waiting for a response. This only appears if you use a centralized version control system like Perforce.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)
Version Control
[](https://docs.unity3d.com/6000.0/Documentation/Manual/perForceIntegration.html)
Perforce Integration
