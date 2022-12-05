# from PyQt6.uic.properties import QtWidgets, QtCore, QtGui
#
# class Affairs(object):
#
#     def initAffairs(self, Mainwindow):
#         self.arrAffairs = []
#
#     def add_item(self):
#         self.Item_n = QtWidgets.QFrame(self.scrollAreaWidgetContents)
#         self.Item_n.setEnabled(True)
#         self.Item_n.setMinimumSize(QtCore.QSize(0, 110))
#         self.Item_n.setMaximumSize(QtCore.QSize(16777215, 16777215))
#         self.Item_n.setStyleSheet("background: rgb(1, 1, 1);")
#         self.Item_n.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
#         self.Item_n.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
#         self.Item_n.setObjectName("Item_n")
#         self.label_n_1 = QtWidgets.QLabel(self.Item_n)
#         self.label_n_1.setGeometry(QtCore.QRect(10, 40, 721, 61))
#         self.label_n_1.setMinimumSize(QtCore.QSize(0, 61))
#         self.label_n_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
#         self.label_n_1.setStyleSheet("background: rgba(225, 225, 225, 150);\n"
#                                      "border-bottom-left-radius: 10px;\n"
#                                      "border-bottom-right-radius: 10px;\n"
#                                      "font-size: 20px;\n"
#                                      "padding: 5px 15px 5px 15px;")
#         self.label_n_1.setTextFormat(QtCore.Qt.TextFormat.AutoText)
#         self.label_n_1.setScaledContents(False)
#         self.label_n_1.setAlignment(
#             QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
#         self.label_n_1.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
#         self.label_n_1.setObjectName("label_43")
#         self.label_n_2 = QtWidgets.QLabel(self.Item_n)
#         self.label_n_2.setGeometry(QtCore.QRect(10, 10, 51, 31))
#         self.label_n_2.setStyleSheet("font-size: 22px;\n"
#                                      "background-color: rgb(125, 232, 109);\n"
#                                      "color: white;\n"
#                                      "border-top-left-radius: 10px;")
#         self.label_n_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
#         self.label_n_2.setObjectName("label_44")
#         self.label_n_3 = QtWidgets.QLabel(self.Item_n)
#         self.label_n_3.setGeometry(QtCore.QRect(60, 10, 671, 31))
#         self.label_n_3.setStyleSheet("background-color: rgb(228, 247, 246);\n"
#                                      "border-top-right-radius: 10px;\n"
#                                      "font-size: 18px;\n"
#                                      "padding-left: 15px;")
#         self.label_n_3.setObjectName("label_45")
#         self.verticalLayout.addWidget(self.Item_n)
#         return self.Item_n
#
#
#     def add_affairs(self, scrollArea):
#         self.arrAffairs.append(self.add_item(self.s))