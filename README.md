# Thinking About Algorithms — interactive companion

A PreTeXt book for Runestone, built around short investigations accompanying Jeff Edmonds's *How to Think About Algorithms*. The first lesson is a complete draft about finding a maximum using a loop invariant. It includes three multiple-choice checkpoints with feedback, an editable Python ActiveCode program, and two explanation/transfer exercises.

## Edit in VS Code

The initial local checkout is `/Users/m/Developer/HowToThinkAboutAlgosCompanion`.

1. Edit `source/lesson-01-maximum.ptx` for lesson text and activities.
2. Press **Cmd+Shift+B** to build the web preview.
3. Choose **Terminal → Run Task → Book: preview (build first)** to serve it locally. The lesson is at `http://localhost:8765/output/web/finding-a-maximum.html`.
4. After edits, build again, then refresh the preview. Saving XML alone does not update the HTML.

The PreTeXt and Live Preview extensions are recommended in `.vscode/extensions.json`. Local VS Code settings select `.venv/bin/python`. Portable build, validation and preview tasks are tracked in `.vscode/tasks.json`.

### Setup on another machine

Python 3.13 was used for the initial setup. Install Node.js/npm for the theme and optional Salve validation engine, then:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
pretext build web
pretext view web --port 8765
```

For the PreTeXt extension, select this environment through `pretext-tools.pythonPath` if it does not detect it. The command tasks call the environment directly and do not require terminal activation. Internet access is needed for first-build dependencies and browser libraries. Student Python examples run in the browser through Runestone's libraries.

## Project map

| File | Purpose |
| --- | --- |
| `source/main.ptx` | Book structure and introduction |
| `source/lesson-01-maximum.ptx` | First lesson: text, questions, feedback and runnable code |
| `source/docinfo.ptx` | Book identifier and catalogue description |
| `publication/publication.ptx` | Ordinary HTML preview settings |
| `publication/runestone.ptx` | Runestone-specific settings |
| `project.ptx` | Web and Runestone build targets |
| `docs/lesson-review.md` | Review prompts and revision record |
| `docs/sources.md` | References and authoring documentation |

Edit the source, not generated `output/` or `published/` files. Preserve question `label` and `xml:id` values after students begin using a course; Runestone associates activity data with exercise identities.

## Review workflow

Read one draft or excerpt, give feedback in chat or make direct edits, then revise and check it. Review accuracy, sequence, accessibility, opportunities to reason, and evidence of learning. The draft has not yet been trialled with students. See `docs/lesson-review.md` for a place to keep decisions.

## Checks

```sh
.venv/bin/pretext validate web --engine salve
.venv/bin/python scripts/check_lesson.py
.venv/bin/pretext build web
.venv/bin/pretext build runestone
```

Salve installs its validator via npm on first use. Multiple-choice elements are classified by PreTeXt as experimental vocabulary even when validation succeeds. Local HTML supports trying the activities; course enrolment, instructor reporting and server-side progress tracking require Runestone hosting. Explanation exercises should be discussed or assessed by a person rather than treated as automatically scored proofs.

## Publish on Runestone

The `runestone` target creates `output/runestone/`. Building it does not publish a course. Runestone administrators must first register the public GitHub repository and give the author access; the author interface then pulls, builds and publishes it. See the [official publishing guide](https://runestone.academy/ns/books/published/pretextguide/sec-publishing-to-runestone-academy.html). Registration has not been requested as part of this draft.

The inherited MIT license for the starter is preserved. Lesson material is newly written; see `docs/sources.md` for attribution and scope.
