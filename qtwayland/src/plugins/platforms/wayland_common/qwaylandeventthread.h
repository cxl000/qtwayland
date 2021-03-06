#ifndef QWAYLANDEVENTTHREAD_H
#define QWAYLANDEVENTTHREAD_H

#include <QObject>
#include <QMutex>
#include <wayland-client.h>

class QSocketNotifier;

class QWaylandEventThread : public QObject
{
    Q_OBJECT
public:
    explicit QWaylandEventThread(QObject *parent = 0);
    ~QWaylandEventThread();

    void displayConnect();

    wl_display *display() const;

private slots:
    void readWaylandEvents();

    void waylandDisplayConnect();

signals:
    void newEventsRead();

private:

    struct wl_display *m_display;
    int m_fileDescriptor;

    QSocketNotifier *m_readNotifier;

    QMutex *m_displayLock;

};

#endif // QWAYLANDEVENTTHREAD_H
