Summary: A log file analysis program
Name: logwatch
Version: 7.3.6
Release: 48.1%{?dist}
License: MIT
Group: Applications/System
URL: http://www.logwatch.org/
Source: ftp://ftp.kaybee.org/pub/linux/logwatch-%{version}.tar.gz
Patch2: logwatch-7.3.1-vsftpd.patch
Patch4: logwatch-7.3.6-secure.patch
Patch5: logwatch-7.3.6-xntpd.patch
Patch6: logwatch-7.3.4-sshd.patch
Patch9: logwatch-7.3.4-sshd3.patch
Patch10: logwatch-7.3.4-named.patch
Patch11: logwatch-7.3.6-named2.patch
Patch12: logwatch-7.3.6-audit.patch
Patch13: logwatch-7.3.6-pam_unix.patch
Patch14: logwatch-7.3.6-named3.patch
Patch15: logwatch-7.3.6-cron.patch
Patch16: logwatch-7.3.6-zz-disk_space.patch
Patch17: logwatch-7.3.6-cron2.patch
Patch18: logwatch-7.3.6-cron3.patch
Patch20: logwatch-7.3.6-secure1.patch
Patch21: logwatch-7.3.6-sudo.patch
Patch22: logwatch-7.3.6-sshd1.patch
Patch23: logwatch-7.3.6-clamav-milter.patch
Patch24: logwatch-7.3.6-conf.patch
Patch26: logwatch-7.3.6-amavis.patch
Patch27: logwatch-7.3.6-oldfiles.patch
Patch28: logwatch-7.3.6-usage.patch
Patch29: logwatch-7.3.6-maillog.patch
Patch30: logwatch-7.3.6-amavis2.patch
Patch31: logwatch-7.3.6-openvpn.patch
Patch32: logwatch-7.3.6-postfix.patch
Patch33: logwatch-7.3.6-cron4.patch
Patch34: logwatch-7.3.6-dovecot_back.patch
Patch35: logwatch-7.3.6-audit2.patch
Patch36: logwatch-7.3.6-openvpn2.patch
Patch37: logwatch-7.3.6-sendmail.patch
Patch38: logwatch-7.3.6-audit3.patch
Patch39: logwatch-7.3.6-init.patch
Patch40: logwatch-7.3.6-cron5.patch
Patch41: logwatch-7.3.6-logrotate.patch
Patch45: logwatch-7.3.6-init2.patch
Patch46: logwatch-7.3.6-secure2.patch
Patch47: logwatch-7.3.6-exim.patch
Patch48: logwatch-7.3.6-zz-disk_space2.patch
Patch49: logwatch-7.3.6-dovecot.patch
Patch50: logwatch-7.3.6-named4.patch
Patch51: logwatch-7.3.6-openvpn3.patch
Patch52: logwatch-7.3.6-smartd.patch
Patch53: logwatch-7.3.6-sshd2.patch
Patch54: logwatch-7.3.6-exim2.patch
Patch55: logwatch-7.3.6-removeservice.patch
Patch56: logwatch-7.3.6-cron_conf.patch
Patch57: logwatch-7.3.6-named5.patch
Requires: textutils sh-utils grep mailx
Requires: perl(Date::Manip)
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArchitectures: noarch

%description
Logwatch is a customizable, pluggable log-monitoring system.  It will go
through your logs for a given period of time and make a report in the areas
that you wish with the detail that you wish.  Easy to use - works right out
of the package on many systems.

%prep
%setup -q
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
rm -f scripts/services/*.orig

%build

%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_var}/cache/logwatch
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/scripts
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/scripts/services
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf/logfiles
install -m 0755 -d %{buildroot}%{_sysconfdir}/logwatch/conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/logfiles
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/default.conf/html 
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/dist.conf/logfiles
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/dist.conf/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/scripts/services
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/scripts/shared
install -m 0755 -d %{buildroot}%{_datadir}/logwatch/lib

for i in scripts/logfiles/*; do
    if [ $(ls $i | wc -l) -ne 0 ]; then
        install -m 0755 -d %{buildroot}%{_datadir}/logwatch/$i
        install -m 0644 $i/* %{buildroot}%{_datadir}/logwatch/$i
    fi
done

install -m 0755 scripts/logwatch.pl %{buildroot}%{_datadir}/logwatch/scripts/logwatch.pl
install -m 0644 scripts/services/* %{buildroot}%{_datadir}/logwatch/scripts/services
install -m 0644 scripts/shared/* %{buildroot}%{_datadir}/logwatch/scripts/shared

install -m 0644 conf/logwatch.conf %{buildroot}%{_datadir}/logwatch/default.conf/logwatch.conf
install -m 0644 conf/logfiles/* %{buildroot}%{_datadir}/logwatch/default.conf/logfiles
install -m 0644 conf/services/* %{buildroot}%{_datadir}/logwatch/default.conf/services
install -m 0644 conf/html/* %{buildroot}%{_datadir}/logwatch/default.conf/html   

install -m 0644 lib/Logwatch.pm %{buildroot}%{_datadir}/logwatch/lib/Logwatch.pm

install -m 0755 -d %{buildroot}%{_mandir}/man8
install -m 0644 logwatch.8 %{buildroot}%{_mandir}/man8

rm -f  %{buildroot}%{_sysconfdir}/cron.daily/logwatch \
   %{buildroot}%{_sbindir}/logwatch \
   %{buildroot}%{_datadir}/logwatch/scripts/services/zz-fortune* \
  %{buildroot}%{_datadir}/logwatch/conf/services/zz-fortune* \
 %{buildroot}%{_datadir}/logwatch/conf/logfiles/fortune*
touch %{buildroot}%{_datadir}/logwatch/scripts/services/zz-fortune
touch %{buildroot}%{_datadir}/logwatch/scripts/services/courier
touch %{buildroot}%{_datadir}/logwatch/scripts/services/dpkg
chmod 644 %{buildroot}%{_datadir}/logwatch/scripts/services/zz-fortune
chmod 644 %{buildroot}%{_datadir}/logwatch/scripts/services/courier
chmod 644 %{buildroot}%{_datadir}/logwatch/scripts/services/dpkg

# install cron script
install -m 0755 -d %{buildroot}%{_sysconfdir}/cron.daily
cat >  %{buildroot}/%{_sysconfdir}/cron.daily/0logwatch <<EOF
#!/bin/bash

DailyReport=\`grep -e "^[[:space:]]*DailyReport[[:space:]]*=[[:space:]]*" /usr/share/logwatch/default.conf/logwatch.conf | head -n1 | sed -e "s|^\s*DailyReport\s*=\s*||"\`

if [ "\$DailyReport" != "No" ] && [ "\$DailyReport" != "no" ]
then
    logwatch
fi
EOF
chmod 755 %{buildroot}/%{_sysconfdir}/cron.daily/0logwatch

install -m 0755 -d %{buildroot}%{_sbindir}
ln -s ../../%{_datadir}/logwatch/scripts/logwatch.pl %{buildroot}/%{_sbindir}/logwatch


echo "###### REGULAR EXPRESSIONS IN THIS FILE WILL BE TRIMMED FROM REPORT OUTPUT #####" > %{buildroot}%{_sysconfdir}/logwatch/conf/ignore.conf
echo "# Local configuration options go here (defaults are in %{_datadir}/logwatch/default.conf/logwatch.conf)" > %{buildroot}%{_sysconfdir}/logwatch/conf/logwatch.conf
echo "# Configuration overrides for specific logfiles/services may be placed here." > %{buildroot}%{_sysconfdir}/logwatch/conf/override.conf


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README HOWTO-Customize-LogWatch
%dir %{_var}/cache/logwatch
%dir %{_sysconfdir}/logwatch
%dir %{_sysconfdir}/logwatch/conf
%dir %{_sysconfdir}/logwatch/scripts
%dir %{_sysconfdir}/logwatch/conf/logfiles
%dir %{_sysconfdir}/logwatch/conf/services
%dir %{_sysconfdir}/logwatch/scripts/services
%dir %{_datadir}/logwatch
%dir %{_datadir}/logwatch/default.conf
%dir %{_datadir}/logwatch/default.conf/services
%dir %{_datadir}/logwatch/default.conf/logfiles
%dir %{_datadir}/logwatch/default.conf/html
%dir %{_datadir}/logwatch/dist.conf
%dir %{_datadir}/logwatch/dist.conf/services
%dir %{_datadir}/logwatch/dist.conf/logfiles
%dir %{_datadir}/logwatch/scripts
%dir %{_datadir}/logwatch/scripts/logfiles
%dir %{_datadir}/logwatch/scripts/services
%dir %{_datadir}/logwatch/scripts/shared
%dir %{_datadir}/logwatch/scripts/logfiles/*
%dir %{_datadir}/logwatch/lib
%{_datadir}/logwatch/scripts/logwatch.pl
%config(noreplace) %{_sysconfdir}/logwatch/conf/*.conf
%config(noreplace) %{_datadir}/logwatch/default.conf/*.conf
%{_sbindir}/logwatch
%{_datadir}/logwatch/scripts/shared/*
%{_datadir}/logwatch/scripts/services/*
%{_datadir}/logwatch/scripts/logfiles/*/*
%{_datadir}/logwatch/lib/Logwatch.pm
%{_datadir}/logwatch/default.conf/services/*.conf
%{_datadir}/logwatch/default.conf/logfiles/*.conf
%{_datadir}/logwatch/default.conf/html/*.html  
%{_sysconfdir}/cron.daily/0logwatch
%doc %{_mandir}/man8/logwatch.8*

%doc License project/CHANGES 

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 7.3.6-48.1
- Rebuilt for RHEL 6

* Tue Aug 11 2009 Ivana Varekova <varekova@redhat.com> 7.3.6-48
- parse a few unmatched entries in named script (#513853)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3.6-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul  7 2009 Ivana Varekova <varekova@redhat.com> 7.3.6-46
- fix cron script

* Thu Jul  2 2009 Ivana Varekova <varekova@redhat.com> 7.3.6-45
- fix cron script

* Thu Jun 25 2009 Ivana Varekova <varekova@redhat.com> 7.3.6-44
- add the possibility to switch of cron job (#493063)

* Mon Jun 15 2009 Ivana Varekova <varekova@redhat.com> 7.3.6-43
- fix removeservice script - to decrease the number of 
  perl instances running simultaneously

* Tue Mar 31 2009 Ivana Varekova <varekova@redhat.com> 7.3.6-42
- fix exim script (#492269)

* Mon Mar 30 2009 Ivana Varekova <varekova@redhta.com> 7.3.6-41
- fix sshd script (#492738)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3.6-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan  6 2009 Ivana Varekova <varekova@redhat.com> 7.3.6-39
- fix smartd script

* Tue Dec 16 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-38
- remove obsolete patches
- fix dovecot,named and openvpn scrpts(#476620)

* Mon Dec  8 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-37
- fix zz-disk_space script (#474810)

* Thu Nov 13 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-35
- fix exim script

* Tue Nov 11 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-34
- fix pam-unix script patches

* Thu Oct 30 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-33
- mark logwatch.conf as a configure file (#468655)

* Wed Oct 29 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-32
- parse another postfix log, do postfix patches cleanup

* Fri Oct 24 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-31
- parse another bunch of postfix logs(#467378)

* Tue Oct 21 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-30
- fix secure, pam_unix and init scripts

* Fri Oct 17 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-29
- fix postfix script again (#462174)

* Mon Sep 15 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-28
- fix postfix script problem
  (#462174)

* Tue Aug 26 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-27
- fix init script problem
  (#459887)

* Fri Aug 15 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-26
- fix problem with changed logrotate suffixes (#458580)

* Wed Aug  6 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-25
- add cron service patch to parse more logs

* Fri Jun 20 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-24
- Resolves: #452044
  handle 2.6.25+ audit messages
- add init script logs parsing

* Tue Jun 10 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-23
- Resolves: #450494
  MailTo configuration parameter is ignored

* Wed Apr 30 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-22
- Resolves: #436719
  Logwatch doesn't show any usable sendmail section

* Fri Apr  4 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-21
- Resolves: #440534 
  Some unmatched OpenVPN log lines
- add parsing of new logw to audit and cron service

* Wed Mar  5 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-20
- Resolves: #436058
  dovecot script for logwatch needs fix for IPv6

* Thu Feb 14 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-19
- resolves cron service problem (#432766)

* Mon Jan 28 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-18
- resolves: #429933 fix postfix script
  thanks Benjamin Gordon

* Mon Jan 21 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-17
- Resolves: #427734
  fix amavis script
- Resolves: #429452
  fix openvpn script

* Tue Jan  8 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-16
- Resolves: #427734
  fix amavis script
- Resolves: #427761
  remove *.orig scripts
- Resolves: #230974
  add no-oldfiles-log option
- remove usage option description
- Resolves: #427596
  fix mailto setting

* Wed Jan  2 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-15
- Resolves: #424171
  logwatch doesn't recognize dovecot starting up message ..

* Wed Jan  2 2008 Ivana Varekova <varekova@redhat.com> 7.3.6-14
- Resolves: #426857
  is report cdrom "disk full" necessary

* Thu Nov 22 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-13
- fix pam_unix script output (#389311)

* Tue Nov 13 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-12
- change Print configuration (#378901)

* Tue Nov  6 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-11
- Resolves: #361921
  fix clamav-milter service

* Tue Oct 30 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-10
- add perl requirement (#356481)

* Fri Oct 12 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-9
- add sshd service patch
- add sudo service patch

* Wed Oct 10 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-8
- add secure service patch

* Wed Oct 10 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-7
- add cron service patch
- add pam-unix service patch

* Thu Aug  9 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-6
- add cron patch

* Tue Jul 10 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-5
- Resolves: #247511
  add zz-disk_space patch

* Tue Jul 10 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-4
- Resolves: #246655
  add cron service patch

* Wed Jul  4 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-3
- add named, pam_unix and audit service patches

* Mon Jun  4 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-2
- fix secure script
- Resolves: #242201
  fix named service

* Tue May 22 2007 Ivana Varekova <varekova@redhat.com> 7.3.6-1
- update to 7.3.6

* Mon May  7 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-8
- add named and sshd service patches

* Fri Apr 20 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-7
- Resolves: 236618 
  (add anacron setting of mailto accept) 
  thanks Todd Denniston

* Fri Apr 13 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-6
- remove another xntpd service logs
- add sshd logs with two spaces after the date tag

* Tue Apr 10 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-5
- logwatch will ignore more useless secure logs

* Wed Apr  4 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-4
- Resolves 234875
  logwatch warns about ntpd startup messages

* Mon Apr  2 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-3
- Resolves: 234767
  Unmatched Entries in mails since sysklogd 1.4.2-3/#223573

* Thu Mar  8 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-2
- add pam_unix service patch

* Tue Feb 20 2007 Ivana Varekova <varekova@redhat.com> 7.3.4-1
- update to 7.3.4

* Mon Feb 12 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-9
- Resolves: 228258
  logwatch warns about dhcdbd subscripton enabled
- add xntpd, up2date and automount services

* Fri Feb  9 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-8
- incorporate the next part of package review comments
- Resolves: 227976
  logwatch warns about auditspd starting

* Thu Feb  8 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-7
- incorporate package review feedback
- Resolves: 227814
  logwatch warns about ntpd deletes interfaces on shutdown

* Mon Feb  5 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-6
- Resolves: 226999
  fix audit script  

* Fri Jan 26 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-5
- add sendmail, automount, amvais and cron patch

* Wed Jan 17 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-4
- add xntpd patch

* Tue Jan 16 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-3
- Resolves: 222263
  sshd script problem

* Fri Jan  5 2007 Ivana Varekova <varekova@redhat.com> 7.3.2-2
- Resolves: 221576
  add html conf files

* Thu Dec 21 2006 Ivana Varekova <varekova@redhat.com> 7.3.2-1
- update to 7.3.2
- remove obsolete patches

* Wed Dec 20 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-9
- add cron, pam_unix, audit, init service patches

* Wed Dec 20 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-8
- add dovecot, amavis and init patch 
- cleanup spec file

* Wed Nov 29 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-7
- add postfix service patch (#208909)
- add vsftpd service patch (#217226)

* Tue Nov 28 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-6
- add automount and mountd service patch

* Wed Nov  1 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-5
- fix named patch (#213267)
- add openvpn patch 

* Mon Oct 30 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-4
- fix #209405 - another sendmail service problem
- fix #212812 - add service script patch 
    patch created by Russell Coker

* Mon Oct 23 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-3
- fix #209405 - sendmail service problems

* Fri Oct 20 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-2
- fix #204078 - missing /etc/logwatch/scripts/services
- add yum service patch
- fix #209554 - automount service problem 

* Fri Oct 20 2006 Ivana Varekova <varekova@redhat.com> 7.3.1-1
- update to 7.3.1

* Tue Aug 29 2006 Ivana Varekova <varekova@redhat.com> 7.3-5
- fix amavis problem #204432 

* Mon Aug 14 2006 Marcela Maslanova <mmaslano@redhat.com> 7.3-4
- add audit patch for SElinux (#200116)
- add patch for sshd (#200105)
- add patch from bugzilla, made by Allen Kistler (#200147)

* Fri Jun 23 2006 Ivana Varekova <varekova@redhat.com> 7.3-3
- added secure-service patch

* Fri May  5 2006 Ivana Varekova <varekova@redhat.com> 7.3-2
- added tests to file creation and access, clean up 
resulting files when logwatch fails (upstream change) 
(#190498)

* Mon Mar 27 2006 Ivana Varekova <varekova@redhat.com> 7.3-1
- update to 7.3
- added samba, up2date

* Fri Mar 17 2006 Ivana Varekova <varekova@redhat.com> 7.2.1-1
- update to 7.2.1
- update nosegfault, pam_unix, http patches
- added sshd, smart, named, audit, secure and mountd services
  patches

* Mon Feb 20 2006 Ivana Varekova <varekova@redhat.com> 7.1-8
- fix http exploit problem #181802

* Fri Jan 20 2006 Ivana Varekova <varekova@redhat.com> 7.1-7
- extended pam_unix patch (fix sshd service)

* Wed Jan 18 2006 Ivana Varekova <varekova@redhat.com> 7.1-6
- removed nounicode patch
- added patch to fix pam_unix logs parsing (#178058)

* Fri Dec 23 2005 Ivana Varekova <varekova@redhat.com> 7.1-5
- fix http exploits problem (bug 176324 - comment 2)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Dec  8 2005 Ivana Varekova <varekova@redhat.com> 7.1-4
- updated /etc/.../logwatch.conf file (bug 175233)

* Tue Nov 29 2005 Ivana Varekova <varekova@redhat.com> 7.1-3
- add secure service patch
- add iptables patch created by Allen Kistler (bug 174954) 
- add audit service patch

* Wed Nov 24 2005 Ivana Varekova <varekova@redhat.com> 7.1-2
- add named script patch (bug 171631)
- change autdated description

* Wed Nov 23 2005 Ivana Varekova <varekova@redhat.com> 7.1-1
- update to 7.1
- added sshd and samba patches

* Wed Nov  2 2005 Ivana Varekova <varekova@redhat.com> 7.0-2
- fix zz-disk_space problem (bug 172230) 
  used michal@harddata.com patch
- fix a few inconsistencies with new directory structure
- changed previous zz-disk_space 
- add secure sript patch allow case insensitivity for GID, UID)

* Thu Oct 13 2005 Ivana Varekova <varekova@redhat.com> 7.0-1
- update to 7.0 (new directory structure)
- add smartd and zz-disk_space patch

* Mon Oct  3 2005 Ivana Varekova <varekova@redhat.com> 6.1.2-7
- add audit script patch recognized other unmatched logs
- add cron script patch 
- change sshd script patch

* Fri Sep 30 2005 Ivana Varekova <varekova@redhat.com> 6.1.2-6
- add audit script patch to recognize number of unmatched entries

* Mon Sep 26 2005 Ivana Varekova <varekova@redhat.com> 6.1.2-5
- change secure script patch
- add sshd script patch (sshd part should not display 0.0.0.0 
   in "Failed to bind" column)
- add one unmatch line to named script

* Mon Sep 19 2005 Ivana Varekova <varekova@redhat.com> 6.1.2-4
- fixed secure script (part of bug 141116, added a few 
  unknown logs)
- bug 168469 - fixed up2date script 

* Mon Jul 25 2005 Ivana Varekova <varekova@redhat.com> 6.1.2-3
- bug 162689 - add noreplace option

* Wed Jun 29 2005 Ivana Varekova <varekova@redhat.com> 6.1.2-2
- fix bug 161973 - The logwatch yum service doesn't properly 
show removed entries
- used patch created by Dean Earley (patch5)

* Thu Jun 23 2005 Ivana Varekova <varekova@redhat.com> 6.1.2-1
- update to 6.1.2-1

* Thu May 19 2005 Jiri Ryska <jryska@redhat.com> 6.0.1-2
- fixed temp dir creation #155795

* Thu Apr 15 2005 Jiri Ryska <jryska@redhat.com> 6.0.1-1
- update to 6.0.1

* Tue Nov 09 2004 Jiri Ryska <jryska@redhat.com>
- Patch for #134288, #138285

* Wed Jul 14 2004 Elliot Lee <sopwith@redhat.com> 5.2.2-1
- Update to 5.2.2
- Patch for #126558, #101744

* Wed Jul 07 2004 Elliot Lee <sopwith@redhat.com> 5.1-6
- Extra patch from #80496

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 24 2004 Joe Orton <jorton@redhat.com> 5.1-4
- stop logging access_log entries with 2xx response codes

* Wed Mar 17 2004 Elliot Lee <sopwith@redhat.com> 5.1-3
- Fix the perl(Logwatch) problem the correct way, as per #118507

* Mon Mar 15 2004 Elliot Lee <sopwith@redhat.com> 5.1-2
- Add provides perl(Logwatch)

* Fri Mar 12 2004 Elliot Lee <sopwith@redhat.com> 5.1-1
- Update (#113802)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Sep 05 2003 Elliot Lee <sopwith@redhat.com> 4.3.2-4
- Fix #103720

* Wed Aug 13 2003 Elliot Lee <sopwith@redhat.com> 4.3.2-3
- Fix a reported bug about MsgsSent/BytesTransferred stats not
  counting locally-originated traffic.

* Wed Jul 10 2003 Elliot Lee <sopwith@redhat.com> 4.3.2-2
- Fix #81144 (nounicode), #85551 and part of #97421 (nosegfault), #87483 (funkyhn)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan 15 2003 Elliot Lee <sopwith@redhat.com> 4.3.1-1
- Update to new upstream version

* Tue Dec 10 2002 Elliot Lee <sopwith@redhat.com> 4.0.3-3
- Apply patch from #77173

* Wed Oct 16 2002 Elliot Lee <sopwith@redhat.com> 4.0.3-2
- Update to new upstream version

* Thu Aug 08 2002 Elliot Lee <sopwith@redhat.com> 2.6-8
- Apply patch from #68804, #68806

* Mon Jul 15 2002 Elliot Lee <sopwith@redhat.com> 2.6-7
- Fix #68869 (the other half of the expandrepeats job)

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 2.6-6
- Remove expandrepeats (#67606)
- Patch6 (ftpd-messages.patch) from #68243

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com> 2.6-5
- logwatch-2.6-applydate-65655.patch to fix xferlog date parsing
- logwatch-2.6-xinetd_match-65856.patch to match more xinetd lines properly
- logwatch-2.6-confparse-65937.patch to properly parse lines with multiple 
  = chars in them

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Apr 15 2002 Elliot Lee <sopwith@redhat.com> 2.6-2
- Fix #62787 (logwatch-2.6-newline-62787.patch) and #63279 (logwatch-2.6-applystddate-63279.patch)

* Sun Mar 31 2002 Elliot Lee <sopwith@redhat.com> 2.6-1
- Don't trust homebaked tempdir creation - always use mktemp.

* Thu Mar 28 2002 Elliot Lee <sopwith@redhat.com> 2.5-4
- Fix the /tmp race for real
- Merge changes from both spec files.

* Thu Mar 28 2002 Kirk Bauer <kirk@kaybee.org> 2.5-2
- Updated new changes from Red Hat's rawhide packaging

* Tue Sep 04 2001 Elliot Lee <sopwith@redhat.com> 2.1.1-3
- Fix #53077

* Thu Aug 09 2001 Elliot Lee <sopwith@redhat.com> 2.1.1-2
- Fix warning in services/init (#51305) and don't include fortune module 
(#51093).

* Mon May 21 2001 Tim Powers <timp@redhat.com>
- updated to 2.1.1
- adapted changes from Kirk Bauer's spec file into this one

* Sat Aug 5 2000 Tim Powers <timp@redhat.com>
- fix bug #15478, spelling error in the description

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jun 8 2000 Tim Powers <timp@redhat.com>
- fixed man page location to be FHS compliant
- use predefined RPM macros whenever possible

* Mon May 15 2000 Tim Powers <timp@redhat.com>
- rebuilt for 7.0

* Mon Jul 19 1999 Tim Powers <timp@redhat.com>
- rebuilt for 6.1

* Thu Apr 15 1999 Michael Maher <mike@redhat.com>
- built package for 6.0
- updated source

* Wed Nov 18 1998 Kirk Bauer <kirk@kaybee.org>
- Modified to comply with RHCN standards

* Fri Oct 2 1998 Michael Maher <mike@redhat.com>
- built package

* Sun Feb 23 1998 Kirk Bauer <kirk@kaybee.org>
- Minor changes and addition of man-page

* Sun Feb 22 1998 Kirk Bauer <kirk@kaybee.org>
- initial release
