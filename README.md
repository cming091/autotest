# usage

> 使用时机: 未知

1. 安装python3，下载最新的版本即可，我用的是3.7.3（版本必须在3.6以上）

2. 安装allure，mac下执行：
    ```sh
    brew install allure

    # 没有安装过brew的，执行下面的命令安装：
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

3. 安装python依赖库，在autotest目录下执行：
    ```sh
    pip3 install -r requirements.txt
    ```

4. 修改autotest/conf/config.ini中的各个section的ip地址，改为自己虚拟机的IP

5. 执行测试，以case/GTP1.0为例，在autotest下执行：
    ```sh
    python3 run.py case/GTP1.0
    ```


# docker 本地运行

> 使用时机：
> 1. 本机装有docker。
> 2. 没有装python
> 3. 或者不想侵扰本机 python/依赖包 版本

1. 制作镜像

    ```sh
    docker build -t mypython:3.7.7 .

    ```

2. 使用镜像运行case

    ```sh

    # 修改 autotest/conf/config.ini
    vi ./conf/config.ini
    # 中的各个section的ip地址，改为自己虚拟机的IP
    # ...
    # 

    # run case
    docker run --rm -it -w /data -v "${PWD}":"/data/" mypython:3.7.7 python run.py -c case/FlipAGV/test_flipagv_out_stock_one_feedline.py


    # run case
    docker run --rm -it -w /data -v "${PWD}":"/data/" mypython:3.7.7 python run.py -c case/FlipAGV/test_flipagv_mock_agv_arrive.py

    ```

3. 删除镜像

    ```sh 

    docker rmi mypython:3.7.7

    ```
4. 本体运行
    运行单个case
        ```
        python3 run.py -c case/TES_V2/test_Avoid_basic.py::TestAvoidBasic::test_avoid_basic_parking
        ```  