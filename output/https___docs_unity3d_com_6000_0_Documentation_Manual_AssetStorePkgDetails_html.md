* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Assets and media](https://docs.unity3d.com/6000.0/Documentation/Manual/assets-and-media.html)
  * [Unity's Asset Store](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)
  * [Publish to the Asset Store](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePublishing.html)
  * Filling in the package details


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreUpload.html)
Uploading assets to your package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreSubmit.html)
Submitting your package for approval
# Filling in the package details
When you [create a package draft](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreCreatePkg.html), the **Create new package** window appears, containing several sections where you can fill out information about your package. These sections are also available every time you edit your package draft, but you must complete all required sections before [submitting your package for approval](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreSubmit.html).
The topics on this page include instructions on how to fill out these sections:
  * [Package Detail](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#Detail)
  * [Metadata & Artwork](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#MetArt)
  * [Package upload](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#upload)
  * [Review](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#Review)
  * [Submit package for approval](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#Submit)


## Package Detail
The **Package Detail** section lets you set the version (with description), category, and price for your package.
![The Package Detail section](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails1.png) The Package Detail section
**Note** : Although the package title appears in the **Package Detail** section, you can only change it in the [Metadata](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#metadata) section.
**Information:** | **Description:**  
---|---  
**Status** | Current status of the package (including **Draft** , **Published** , **Declined** , and **Pending**).  
**Version** | The version number for your package (such as 1.5, 1.6, 1.7). New Asset Store packages should use the default version 1.0.  
  
When you release updates for your Assets, you can increment the version number here. For example, if you need to fix a bug, change the minor version number (1.3 to 1.4). If you introduce a big change, change the major version (1.3 to 2.0).  
**Version Changes** | Describe any updates that triggered a version change, such as bug fixes, new Assets, or changes to match a new version of Unity.  
**Category** | Choose a category that best fits your package, because when customers look for Assets on the **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore), they can filter the list of packages by the category that you choose. If you’re not sure which category to choose, go to the [main page of the Asset Store](https://assetstore.unity.com/) and see what types of Assets are available in similar categories.  
**Price USD** | You can set a price of $4.99 or any higher amount in US dollars. For any lower price, enable **Free** instead.  
When you’re finished, click **Save**.
## Metadata & Artwork
The **Metadata & Artwork** section lets you set the name of the package and include marketing images, audio, and video to add branding for your package.
![The Metadata & Artwork section](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails2.png) The Metadata & Artwork section
The artwork ([key images](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#image), [audio/video](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#audvid), and [screenshots](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#shots)) are shared across all languages.
You must set an English [name and description](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#metadata). You can also specify a name and description in Japanese, Korean, and Chinese. To do this, click the links under the **Language** column. When you add a language, a new **Edit** link appears under the **Metadata** column for that language.
You can only edit **Tags** after your package has been accepted for publishing.
### Metadata
Metadata includes the name, description, and keywords for your package, so customers can find your package while they’re browsing or searching the Asset Store.
To edit the name and description of your package:
  1. In the **Metadata & Artwork** section, under **Metadata** , click the **Edit** button.
The **Metadata** page for a specific language appears:
![Set the Title, Description, and Keywords on the English Metadata page](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails2a.png) Set the **Title** , **Description** , and **Keywords** on the English Metadata page
  2. Enter the **Title** of your package (required). The title shouldn’t begin with the word “Unity” if possible. For example, you can’t use “Unity Sculpting Tools,” but you can use “Sculpting Tools for Unity.”
  3. Enter a package **Description** :
     * If your package has 3D Assets, include information about the polygon count, the Texture size, and which rendering pipeline is compatible.
     * If your package has **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and tools, mention any dependencies needed for the Asset (for example, another Asset or third-party software), because you can’t add them to the Asset Store package and the user needs to import them separately.
You can decorate this text with any of the following HTML tags:
     * **EM** (for italics). For example: `This is for <EM>italicized</EM> text`.
     * **STRONG** (for bold). For example: `This is for <STRONG>bold</STRONG> text`.
     * **A** (for hyperlinks). For example: `This links <A HREF="http://www.example.com">here</A>`.
     * **P** (to define a paragraph). For example: `<P>This is a new paragraph</P>`.
     * **BR** (for a line break). For example: `This is the first line.</BR>This text appears on the next line`.
  4. You can optionally add a list of **Keywords** separated by whitespace to influence your Asset’s results in Asset Store searches. There is a limit of 255 characters.
  5. Click **Save** when you’re finished and then click **OK** when the dialog appears.
  6. To return to the **Package** window, click **Go Back**.


### Key image
Key images should indicate what your Asset Store package does and help it stand out. You can set four different resolutions so that your key images appear as icons or thumbnails when customers browse or filter the list of packages available in the Asset Store, and as larger images on the main product page or on social media. These also might appear in promotional material.
Here are some general requirements for the images you upload in this section:
  * The images can’t contain the following: 
    * Unity logos
    * Sale banners
    * The default Unity **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) (for example, as a background)
  * The images must not be blurry, stretched, or cropped.
  * The images can’t only be screenshots of the Unity Editor.
  * You should make different designs for images of different sizes so that the objects or visuals in the icon and card images are legible and separate.


This table describes the different images, where they might appear on the Asset Store and specific requirements for each:
**Key Image Type:** | **Size (in pixels):** | **Description:**  
---|---|---  
**Icon** | 160 x 160 | The Icon image is visible while users are browsing the Asset Store using the [icon grid layout](https://assetstore.unity.com/?category=3d%2Fanimations&orderBy=1). This image shouldn’t contain text.  
  
**Note:** Icon images must be 160x160, even though the actual display size is 80x80. At 80x80, image text isn’t readable, but uploading the larger size lets the Asset Store display icons clearly at the smaller size.  
**Card** | 420 x 280 | This is the main thumbnail visible on your Home page and the default view [while browsing](https://assetstore.unity.com/?category=3d&orderBy=1) the Asset Store. This image can have only the following text:   
- Title of the Asset  
- Logo or name of the publisher  
  
**Note:** Like icon images, you must upload Card images at a larger size (420x280) than the size of image that appears on the Asset Store.  
**Cover** | 1950 x 1300 | This is what customers see on the main product page for your package. This image can have only the following text:   
- Title of the Asset  
- Logo or name of the publisher  
- A tag line  
  
**Note:** Like icon images, you must upload Cover images at a larger size (1950x1300) than the size of image that appears on the Asset Store.  
**Social Media** | 1200 x 630 | The Unity community team might post these images to social media, or on the Asset Store home page. This image shouldn’t contain text.  
For more information, refer to the [Asset Store FAQ](https://support.unity3d.com/hc/en-us/articles/210122403-What-makes-a-great-key-image-).
To set one or more key images:
  1. In the **Metadata & Artwork** section, under the **Key Images** column, click the **Edit** button.
The Key Images page appears:
![Set the Icon, Care, Cover, and Social Media images on the Key Images page](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails2b.png) Set the **Icon** , **Care** , **Cover** , and **Social Media** images on the Key Images page
  2. To upload an image, click **Choose File** or drag the image onto the gray box.
**Note:** The image must be the exact size as indicated.
The uploaded image appears with a **Remove** button under it, which you can click if you need to remove that image.
  3. To return to the **Package** window, click **Go Back**.


### Audio/Video
You can upload audio or video files that display what your Asset Store package does or has. These are available on your main product page (as thumbnails you can click on to play).
**Note:** If your package has audio or video files, you must upload samples of your media Assets here. If your package has tools, scripting, or other technical Assets, include a video tutorial explaining the setup process, and give an overview of your Asset’s functionality. If your package has animations, include a video of all the available animations.
You can embed uploaded files in the show reel with the screenshots of your package. Audio and video files can come from either your local computer or device, or you can specify links to any of these services:
  * [YouTube](https://www.youtube.com/)
  * [Vimeo](https://vimeo.com/)
  * [SoundCloud](https://soundcloud.com/)
  * [MixCloud](https://www.mixcloud.com/)
  * [SketchFab](https://sketchfab.com/)


To set one or more key images:
  1. In the **Metadata & Artwork** section, under the **Audio/Video** column, click the **Edit** button.
The Audio/Video page appears:
![Add audio or video files or a link to online media on the Audio/Video page](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails2c.png) Add audio or video files or a link to online media on the Audio/Video page
  2. You can upload audio or video files using any of these methods:
     * Drag the file onto the gray box.
     * Click **Choose File** to select the file from a file browser.
     * Enter a link to an online file in the text box and click **Upload link**.
The uploaded image appears with a **Remove** button under it.
  3. To return to the **Package** window, click **Go Back**.


### Screenshots
You can upload screenshots of your package’s Assets in action. These are available on your main product page (as thumbnails you can click on to enlarge).
Screenshots are just as important as [key images](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStorePkgDetails.html#image) when trying to sell your package. Screenshots showcase your package, showing users how it works and what it can do. Users often use screenshots as a kind of package preview before they actually buy it. Asset Store curators prefer having screenshots for most Assets. For example, if it’s a Model, add images that display the Asset from different perspectives, both fully textured and in wireframe.
To set one or more screenshots:
  1. Click the **Edit** button under the **Screenshots** section.
The Screenshots page appears:
![Add screenshots from your package on the Screenshots page](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails2d.png) Add screenshots from your package on the Screenshots page
  2. You can upload one or more screenshots using either of these methods:
     * Drag the file onto the gray box.
     * Click **Choose File** to select the file from a file browser.
The uploaded image appears with a red **X** icon (to remove it) under it.
  3. To return to the **Package** window, click **Go Back**.


## Package upload
The **Package upload** section lets you launch Unity directly after having created a package draft or editing package draft details. 
![Before you upload Assets to your package draft, the Launch Unity button appears](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails3.png) Before you upload Assets to your package draft, the Launch Unity button appears
When you click the **Launch Unity** button, your Project appears in the Unity Editor if Unity is already open. If not, the Hub opens, allowing you to choose which Project to open.
If you have already uploaded Assets to your package draft, they appear in this section with the **Remove** and **Edit** buttons:
![After you upload Assets to your package draft, the package appears with Remove and Edit buttons](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails3a.png) After you upload Assets to your package draft, the package appears with Remove and Edit buttons
If you want to clear the Assets from your package, click the **Remove** button.
Before submitting the package for approval, click the **Edit** button.
![Settings details for your package.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails3b.png) Settings details for your package.
For each section, select **Yes** to display a question and a set of checkboxes. Then check or uncheck the options that answer the questions about your package. When you’re finished, click **Save** to return to the **Package upload** section.
For more information about adding and uploading Assets into your package draft, refer to [Uploading Assets to your package](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreUpload.html).
## Review
Under the **Review** section, click **Preview in Asset Store** to see how your package will look in the Asset Store after publishing it. You can also see a preview of the URLs under **Public links** :
![The Review section displays a button to preview your package draft on the Asset Store](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails4.png) The Review section displays a button to preview your package draft on the Asset Store
## Submit package for approval
Under the **Submit package for approval** section, click **Auto publish** to indicate whether you want the package to appear in the Asset Store directly after Unity approval.
You also have to confirm whether you own the rights to sell the Assets.
![If you havent uploaded any Assets to your package yet, a message warns you to upload some](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/AssetStorePkgDetails5.png) If you haven’t uploaded any Assets to your package yet, a message warns you to upload some
For detailed instructions, refer to [Submitting your package for approval](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreSubmit.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreUpload.html)
Uploading assets to your package
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStoreSubmit.html)
Submitting your package for approval
