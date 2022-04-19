# juan

`juan` generates `.gitignore` files for different programming languages or platforms from the command line.

![](https://i.imgur.com/wq4NuuO.gif)

Inspired by [joe](https://github.com/karan/joe), but following the [Command Line Interface Guidelines](https://clig.dev/#guidelines) and adding autocompletion (at some point). So, think of `juan` as a distant cousin of `joe`.

## Installation

### Install from PyPi

```shell
pip install juan
```

After install run `juan -u` to update the available list of `.gitignore` files. This command will download the files in these locations:

* macOS: `/Users/<your-user>/Library/Application Support/juan`
* Windows: `C:\\Users\\<your-user>\\AppData\\Local\\juan\\juan`
* Linux: `/home/<your-user>/.local/share/juan`

## Usage

Update the list of avilable `.gitignore` files:

```shell
$ juan -u
Updating gitignore files...
252 .gitignore files:
actionscript, ada, agda, al, al, altiumdesigner, android, anjuta, ansible, appceleratortitanium, appengine, archives, archlinuxpackages, atmelstudio, autoit, autotools, b4x, backup, bazaar, bazel, beef, bitrix, bricxcc, c, c++, cakephp, calabash, cdk, cfwheels, chefcookbook, clojure, cloud9, cmake, codeigniter, codekit, codesniffer, commonlisp, composer, concrete5, coq, cordova, core, craftcms, cuda, cvs, d, dart, darteditor, delphi, diff, dm, dreamweaver, dropbox, drupal, drupal7, eagle, eclipse, eiffelstudio, elisp, elixir, elm, emacs, ensime, episerver, erlang, esp-idf, espresso, exercism, expressionengine, extjs, fancy, finale, flaxengine, flexbuilder, forcedotcom, fortran, fuelphp, gcov, gitbook, gnomeshellextension, go, go.allowlist, godot, gpg, gradle, grails, gretl, gwt, haskell, hugo, iar_ewarm, idris, igorpro, images, inforcms, java, jboss, jboss4, jboss6, jdeveloper, jekyll, jenkins_home, jenv, jetbrains, jigsaw, joomla, julia, jupyternotebooks, kate, kdevelop4, kentico, kicad, kohana, kotlin, labview, laravel, lazarus, leiningen, lemonstand, lensstudio, libreoffice, lilypond, linux, lithium, logtalk, lua, lyx, macos, magento, magento1, magento2, matlab, maven, mercurial, mercury, metals, metaprogrammingsystem, meteor, microsoftoffice, modelsim, momentics, monodevelop, nanoc, nasaspecsintact, netbeans, nikola, nim, ninja, nix, node, notepadpp, nwjs, objective-c, ocaml, octave, opa, opencart, openssl, oracleforms, otto, packer, patch, perl, phalcon, phoenix, pimcore, playframework, plone, prestashop, processing, psoccreator, puppet, purescript, putty, python, qooxdoo, qt, r, racket, racket, rails, raku, red, redcar, redis, rhodesrhomobile, ros, ros2, ruby, rust, sam, sass, sbt, scala, scheme, scons, scrivener, sdcc, seamgen, sketchup, slickedit, smalltalk, snap, spfx, splunk, stata, stella, strapi, sublimetext, sugarcrm, svn, swift, symfony, symphonycms, syncthing, synopsysvcs, tags, terraform, tex, textmate, textpattern, thinkphp, toit, tortoisegit, turbogears2, twincat3, typo3, umbraco, unity, unrealengine, uvision, v, vagrant, vim, virtualenv, virtuoso, visualstudio, visualstudiocode, vue, vvvv, waf, webmethods, windows, wordpress, xcode, xilinx, xilinxise, xojo, yeoman, yii, zendframework, zephir
```

View available files:

```shell
$ juan -ls
252 .gitignore files:
actionscript, ada, agda, al, al, altiumdesigner, android, anjuta, ansible, appceleratortitanium, appengine, archives, archlinuxpackages, atmelstudio, autoit, autotools, b4x, backup, bazaar, bazel, beef, bitrix, bricxcc, c, c++, cakephp, calabash, cdk, cfwheels, chefcookbook, clojure, cloud9, cmake, codeigniter, codekit, codesniffer, commonlisp, composer, concrete5, coq, cordova, core, craftcms, cuda, cvs, d, dart, darteditor, delphi, diff, dm, dreamweaver, dropbox, drupal, drupal7, eagle, eclipse, eiffelstudio, elisp, elixir, elm, emacs, ensime, episerver, erlang, esp-idf, espresso, exercism, expressionengine, extjs, fancy, finale, flaxengine, flexbuilder, forcedotcom, fortran, fuelphp, gcov, gitbook, gnomeshellextension, go, go.allowlist, godot, gpg, gradle, grails, gretl, gwt, haskell, hugo, iar_ewarm, idris, igorpro, images, inforcms, java, jboss, jboss4, jboss6, jdeveloper, jekyll, jenkins_home, jenv, jetbrains, jigsaw, joomla, julia, jupyternotebooks, kate, kdevelop4, kentico, kicad, kohana, kotlin, labview, laravel, lazarus, leiningen, lemonstand, lensstudio, libreoffice, lilypond, linux, lithium, logtalk, lua, lyx, macos, magento, magento1, magento2, matlab, maven, mercurial, mercury, metals, metaprogrammingsystem, meteor, microsoftoffice, modelsim, momentics, monodevelop, nanoc, nasaspecsintact, netbeans, nikola, nim, ninja, nix, node, notepadpp, nwjs, objective-c, ocaml, octave, opa, opencart, openssl, oracleforms, otto, packer, patch, perl, phalcon, phoenix, pimcore, playframework, plone, prestashop, processing, psoccreator, puppet, purescript, putty, python, qooxdoo, qt, r, racket, racket, rails, raku, red, redcar, redis, rhodesrhomobile, ros, ros2, ruby, rust, sam, sass, sbt, scala, scheme, scons, scrivener, sdcc, seamgen, sketchup, slickedit, smalltalk, snap, spfx, splunk, stata, stella, strapi, sublimetext, sugarcrm, svn, swift, symfony, symphonycms, syncthing, synopsysvcs, tags, terraform, tex, textmate, textpattern, thinkphp, toit, tortoisegit, turbogears2, twincat3, typo3, umbraco, unity, unrealengine, uvision, v, vagrant, vim, virtualenv, virtuoso, visualstudio, visualstudiocode, vue, vvvv, waf, webmethods, windows, wordpress, xcode, xilinx, xilinxise, xojo, yeoman, yii, zendframework, zephir
```

Generate a `.gitignore` file for a project using Linux and Vim:

```shell
$ juan -g vim,linux > .gitignore
```

Output in the `.gitignore` file generated:

```shell
#### juan made this: https://github.com/j0lv3r4/juan ####

### Vim ###

# Swap
[._]*.s[a-v][a-z]
!*.svg  # comment out if you don't need vector files
[._]*.sw[a-p]
[._]s[a-rt-v][a-z]
[._]ss[a-gi-z]
[._]sw[a-p]

# Session
Session.vim
Sessionx.vim

# Temporary
.netrwhist
*~
# Auto-generated tag files
tags
# Persistent undo
[._]*.un~

#### juan made this: https://github.com/j0lv3r4/juan ####

### Linux ###

*~

# temporary files which can be created if a process still has a handle open of a deleted file
.fuse_hidden*

# KDE directory preferences
.directory

# Linux trash folder which might appear on any partition or disk
.Trash-*

# .nfs files are created when an open file is removed but is still being accessed
.nfs*
```

Append to an existing `.gitignore` file:

```shell
$ juan -g vim,linux >> .gitignore
```
