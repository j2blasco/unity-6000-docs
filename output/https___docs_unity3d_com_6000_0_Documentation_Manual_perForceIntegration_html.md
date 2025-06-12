* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/perForceIntegration.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Version Control](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)
  * Perforce Integration


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Versioncontrolintegration.html)
Version control integrations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SmartMerge.html)
Smart merge
# Perforce Integration
For more information on **Perforce** , visit [www.perforce.com](https://www.perforce.com/downloads/helix).
## Setting up Perforce
Follow the setup process described in the [Version Control](https://docs.unity3d.com/6000.0/Documentation/Manual/Versioncontrolintegration.html)A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and PlasticSCM. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VersionControl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VersionControl) documentation. See [Perforce documentation](https://www.perforce.com/perforce/doc.current/manuals/p4v/) if you encounter any problems.
**Note** : If your Perforce workspace has multi-factor authentication enabled you will first need to login through the command line using _p4 login2_ or by using a visual client like P4V to be able to login in the Unity Editor as well.
## Working offline with Perforce
Only use this if you know how to work offline in Perforce without a Sandbox. Refer to the [Perforce documentation](https://www.perforce.com/manuals/p4v/Content/P4V/using.offline.html) for further information.
## Troubleshooting
If Unity cannot commit your changes to Perforce (for example, if the server is down, or you experience licensing issues), your changes are stored in a separate changeset. If the console doesn’t list any info about the issue, you can use the P4V client for Perforce to submit this changeset to see the exact error message.
You cannot submit changes if you are sharing a workspace with another user. A workspace should be dedicated to one user only.
## Automatic revert of unchanged files on submit
It’s possible to configure Perforce to revert unchanged files on submit. To do this in P4V, select **Connection** > **Edit Current Workspace** , view the **Advanced** tab and set the value of **On submit** to **Revert unchanged files**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Versioncontrolintegration.html)
Version control integrations
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SmartMerge.html)
Smart merge
