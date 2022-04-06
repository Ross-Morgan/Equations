from __future__ import annotations

import sys
from typing import Callable

from PyQt6 import QtCore, QtGui, QtWidgets

from assets import Assets, load_config

default_boxes = "default-boxes"
default_const = "default-const"
superscript = ["", "x", "x²", "x³", "x⁴"]


class PolyBox(QtWidgets.QFrame):
    def __init__(self, exp: int, id: str, const: str, *,
                 parent: QtWidgets.QWidget) -> None:
        """
        A frame containing an input box and a label

        ---

        - @param exp: int [ Polynomial degree for box label]
        - @param id: str [ Letter relating each coefficient ]
        - @param const: str [ Letter relating to the indeterminate ]
        - @param parent: QWidget [ Graphical interface to embed into ]
        """
        super().__init__(parent)

        self.exp = exp
        self.id = id
        self.const = const
        self.label = f"{self.const}{superscript[self.exp]}"

        self.setup_ui()

    def setup_ui(self):
        box_input = QtWidgets.QLineEdit()
        box_input.setPlaceholderText(self.id)

        box_label = QtWidgets.QLabel()
        box_label.setText(self.label)

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(box_input)
        layout.addWidget(box_label)


PBoxFunc = Callable[[PolyBox], None] | Callable[[PolyBox, int], None]


class PolyBoxes:
    __id_order = ["edcba"]

    def __init__(self, n: int, const: str, *, parent: QtWidgets.QWidget):
        assert 5 >= n > 1, "Must have 2-5 (inc.) boxes"

        self.p_boxes = []
        self.const = const

        id_order = self.__id_order[-1 - n + 1: n]

        for exponent, id in zip(range(0, n, -1), id_order):
            self.p_boxes.append(
                PolyBox(exp=exponent, id=id, const=const, parent=parent)
            )

        self.layout = QtWidgets.QHBoxLayout(parent)

        self.for_all_boxes(self.layout.addWidget)

    def for_all_boxes(self, func: PBoxFunc, *, pass_id: bool = False):
        """
        A function that takes a box and the box's id and returns `None`

        ---

        - @param func: Callable[[PolyBox, int], None]
        - @param pass_id: bool
        """
        for i, p_box in enumerate(self.p_boxes):
            args = (i,) if pass_id else ()
            func(p_box, *args)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, size: QtCore.QSize, title: str, icon: QtGui.QIcon, *,
                 parent: QtWidgets.QWidget = None, **config) -> None:
        super().__init__(parent)

        self.config = config
        self.poly_boxes = None

        self.resize(size)
        self.setWindowTitle(title)
        self.setWindowIcon(icon)

        self.setup_ui()

    def setup_ui(self) -> None:
        self.background = QtWidgets.QLabel(self)
        self.background.resize(self.size())
        self.background.move(0, 0)
        self.background.setStyleSheet(Assets.Styles.background)

        self.p_boxes_container = QtWidgets.QLabel(self)
        self.p_boxes_container.setGeometry(20, 20, 600, 200)
        self.p_boxes_container.setStyleSheet(Assets.Styles.poly_box_container)

        self.reset_poly_boxes(
            n=self.config.pop(default_boxes),
            const=self.config.pop(default_const)
        )

    def reset_poly_boxes(self, n: int, const: str) -> None:
        self.poly_boxes = PolyBoxes(n, const, parent=self.p_boxes_container)


@load_config("../config/config.yaml")
def main(config: dict):
    app = QtWidgets.QApplication(sys.argv)

    size = QtCore.QSize(*map(int, config.pop("size")))
    title: str = config.pop("title")
    icon = QtGui.QIcon(config.pop("icon"))

    window = MainWindow(size, title, icon, **config)
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
