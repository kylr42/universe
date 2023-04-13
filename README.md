![Copier template](https://img.shields.io/badge/template%20engine-copier-informational)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/lincc-frameworks/python-project-template/ci.yml)
![Read the Docs](https://img.shields.io/readthedocs/lincc-ppt)

# Universe Copier Template

This project template simplifies creating new projects and facilitating maintaining existing projects by standardizing their structure. Using such a project enhances efficiency and reduces development time for Python projects.

## Example

This is an example of how the template will look like after generation. 

![example](images/example.gif)

> [Copier](https://copier.readthedocs.io/en/latest/) is required to use this template. Copier is an open source tool that hydrates projects from templates and natively supports updating projects as the original template matures. It's really neat!
>
> See the detailed user guide in [readthedocs](https://lincc-ppt.readthedocs.io/) for more information.


This project itself is just the template, but you need to install these tools to use it:

- [Copier](https://copier.readthedocs.io/en/latest/)
- [git](https://git-scm.com/) 2.24 or newer
- [python](https://www.python.org/) 3.7+

## Getting started

Choose where you would like to create your new project, and call copier with the template.

```bash
>$ python3 -m pip install copier
>$ copier gh:kylr42/universe ~/path/to/your/subproject
```

Copier will ask you a lot of questions. Answer them to properly generate the template.

## Updating

If you always used Copier with this project, getting last updates with Copier is simple:

```bash
cd ~/path/to/your/downstream/scaffolding
copier update
```

Copier will ask you all questions again, but default values will be those you answered
last time. Just hit <kbd>Enter</kbd> to accept those defaults, or change them if
needed... or you can use `copier --force update` instead to avoid answering again all
things.

Basically, read Copier docs and `copier --help-all` to know how to use it.

## Go Directories after generation

### `/app`

Main application directory. This is where the main application code is stored. 

### `/app/internal`

Private application and library code. This is the code you don't want others importing in their applications or libraries. Note that you are not limited to the top level `app/internal` directory. You can have more than one `app/internal` directory at any level of your project tree.

You can optionally add a bit of extra structure to your internal packages to separate your shared and non-shared internal code. It's not required (especially for smaller projects), but it's nice to have visual clues showing the intended package use. Your actual application code can go in the `app/internal` directory and the code shared by those apps in the `app/internal/pkg` directory (e.g., `app/internal/pkg/middlewares`).

### `/app/pkg`

Library code that's ok to use by external applications (e.g., `app/pkg/connectors`). Other projects will import these libraries expecting them to work, so think twice before you put something here :-) 

The `app/pkg` directory is still a good way to explicitly communicate that the code in that directory is safe for use by others. 

### `/scripts`

Scripts to perform various build, install, analysis, etc operations. 

### `/configs`

Configuration file templates or default configs.

### `/tests`

Additional external test apps and test data. Feel free to structure the `/tests` directory anyway you want. For bigger projects it makes sense to have a data subdirectory. For example, you can have `/tests/data` or `/tests/testdata` if you need Go to ignore what's in that directory.

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

This project is licensed under the terms of the [MIT License](LICENSE).

## Credits

This project was created with [Copier](https://copier.readthedocs.io/).
