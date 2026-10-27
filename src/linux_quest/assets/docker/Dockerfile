FROM rockylinux/rockylinux:8
LABEL org.linux-quest.image-version="2026.1"
RUN sed -i '/tsflags=nodocs/d' /etc/yum.conf && \
    dnf -y --allowerasing install bash coreutils findutils grep sed gawk tar gzip bzip2 xz zip unzip \
      vim-minimal nano procps-ng man-db man-pages shadow-utils sudo file iproute \
      iputils bind-utils which diffutils less python3 rpm-build curl && \
    dnf clean all && \
    useradd -m -u 1000 -s /bin/bash learner && \
    groupadd archive && usermod -aG archive learner && \
    printf 'learner ALL=(root) NOPASSWD: /usr/sbin/useradd, /usr/sbin/groupadd, /usr/sbin/usermod, /usr/bin/chown, /usr/bin/chgrp, /usr/bin/rpm, /usr/bin/renice\n' > /etc/sudoers.d/quest && \
    chmod 440 /etc/sudoers.d/quest
COPY quest-helper.py /usr/local/bin/quest
COPY bashrc /opt/quest/bashrc
COPY checks.py /opt/quest/checks.py
COPY snapshot.py /opt/quest/snapshot.py
COPY demo.spec /tmp/demo.spec
RUN chmod 755 /usr/local/bin/quest && \
    rpmbuild -bb /tmp/demo.spec && mkdir -p /opt/quest/packages /opt/quest-network && \
    cp /root/rpmbuild/RPMS/noarch/*.rpm /opt/quest/packages/ && \
    printf 'ARCHIVE_OK\n' > /opt/quest-network/status.txt && \
    rm -rf /root/rpmbuild /tmp/demo.spec
ENV LANG=C.UTF-8 TERM=xterm-256color
USER learner
WORKDIR /home/learner
CMD ["sleep", "infinity"]
