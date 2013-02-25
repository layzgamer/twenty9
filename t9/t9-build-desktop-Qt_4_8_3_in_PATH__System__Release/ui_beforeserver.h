/********************************************************************************
** Form generated from reading UI file 'beforeserver.ui'
**
** Created: Fri Feb 15 19:43:05 2013
**      by: Qt User Interface Compiler version 4.8.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BEFORESERVER_H
#define UI_BEFORESERVER_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QDialog>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLabel>
#include <QtGui/QLineEdit>
#include <QtGui/QPushButton>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QHBoxLayout *horizontalLayout;
    QLabel *label;
    QLineEdit *Name;
    QPushButton *Create;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->setWindowModality(Qt::ApplicationModal);
        Dialog->resize(431, 41);
        horizontalLayout = new QHBoxLayout(Dialog);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label = new QLabel(Dialog);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout->addWidget(label);

        Name = new QLineEdit(Dialog);
        Name->setObjectName(QString::fromUtf8("Name"));

        horizontalLayout->addWidget(Name);

        Create = new QPushButton(Dialog);
        Create->setObjectName(QString::fromUtf8("Create"));

        horizontalLayout->addWidget(Create);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("Dialog", "Name", 0, QApplication::UnicodeUTF8));
        Create->setText(QApplication::translate("Dialog", "Create", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BEFORESERVER_H
