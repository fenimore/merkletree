# Merkel Tree

## Example Output

### File System

> $ python filesystem.py root

    Merkel Tree File System
    61d6f3bcc601922f4bdb28c68ffbff5f | root
    e837b2a534651a08975d541962e32958 | root/file.txt
    d8b4e7094e01a00ac3ee2ebd73e853bf | root/video.vid
    3e9de4edd847a70e4250712fa1d92b17 | root/alpha
    69c3d3dcb18c44e1d6018728c98036e5 | root/alpha/alpha.txt
    6874bad209db16eefb97ce9f1728890a | root/alpha/sub
    bec4c5134ad0d0a1c9a48fffe76f9085 | root/alpha/sub/delta.txt
    0796cf21848318a9d62e3ab00faacba2 | root/alpha/empty
    628a8bcec58efd0f40ad76cc536ed174 | root/beta
    da629b389ee4c44f433493e58d06cca6 | root/beta/beta.txt


After removing a file

    Merkel Tree File System
    fb55b2e94229b9793cd691b28411bf23 | root
    e837b2a534651a08975d541962e32958 | root/file.txt
    d8b4e7094e01a00ac3ee2ebd73e853bf | root/video.vid
    4bf05ef8aa7cdcae8c2a2b63f2f93bdc | root/alpha
    69c3d3dcb18c44e1d6018728c98036e5 | root/alpha/alpha.txt
    51da37e6f3253e5d7799304d8ae2b43d | root/alpha/sub
    0796cf21848318a9d62e3ab00faacba2 | root/alpha/empty
    628a8bcec58efd0f40ad76cc536ed174 | root/beta
    da629b389ee4c44f433493e58d06cca6 | root/beta/beta.txt
