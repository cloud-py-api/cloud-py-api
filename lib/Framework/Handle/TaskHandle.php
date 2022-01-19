<?php

declare(strict_types=1);

/**
 * @copyright Copyright (c) 2021 Andrey Borysenko <andrey18106x@gmail.com>
 * 
 * @copyright Copyright (c) 2021 Alexander Piskun <bigcat88@icloud.com>
 * 
 * @author 2021 Andrey Borysenko <andrey18106x@gmail.com>
 *
 * @license AGPL-3.0-or-later
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

namespace OCA\Cloud_Py_API\Framework\Handle;

use OCP\IConfig;

use OCA\Cloud_Py_API\Proto\PBEmpty;
use OCA\Cloud_Py_API\Proto\TaskExitRequest;
use OCA\Cloud_Py_API\Proto\TaskInitReply;
use OCA\Cloud_Py_API\Proto\TaskInitReply\cfgOptions;
use OCA\Cloud_Py_API\Proto\TaskLogRequest;
use OCA\Cloud_Py_API\Proto\TaskSetStatusRequest;

use OCA\Cloud_Py_API\AppInfo\Application;
use OCA\Cloud_Py_API\Framework\Manager\QueriesManager;
use OCA\Cloud_Py_API\Proto\dbConfig;
use OCA\Cloud_Py_API\Proto\logLvl;
use OCA\Cloud_Py_API\Service\AppsService;
use OCA\Cloud_Py_API\Service\ServerService;
use Psr\Log\LoggerInterface;


class TaskHandle {

	/** @var IConfig */
	private $config;

	/** @var AppsService */
	private $appsService;

	/** @var LoggerInterface */
	private $logger;

	public function __construct(IConfig $config, AppsService $appsService, LoggerInterface $logger) {
		$this->config = $config;
		$this->appsService = $appsService;
		$this->logger = $logger;
	}

	/**
	 * Task initialization
	 * 
	 * @param PBEmpty $request
	 * 
	 * @return TaskInitReply|null
	 */
	public function init(PBEmpty $request): ?TaskInitReply {
		$taskInitReply = new TaskInitReply();
		if (ServerService::$APP !== null) {
			if (isset(ServerService::$APP['appname'])) {
				$taskInitReply->setAppName(ServerService::$APP['appname']);
			}
			if (isset(ServerService::$APP['modname'])) {
				$taskInitReply->setModName(ServerService::$APP['modname']);
			}
			if (isset(ServerService::$APP['modpath'])) {
				$taskInitReply->setModPath(ServerService::$APP['modpath']);
			}
			if (isset(ServerService::$APP['funcname'])) {
				$taskInitReply->setFuncName(ServerService::$APP['funcname']);
			}
			if (isset(ServerService::$APP['args'])) {
				$taskInitReply->setArgs(ServerService::$APP['args']);
			}
			$cfg = new cfgOptions();
			$cfg->setLogLvl(logLvl::value(logLvl::name($this->config->getSystemValue('loglevel'))));
			$cfg->setDataFolder($this->config->getSystemValue('datadirectory'));
			$cfg->setFrameworkAppData($this->appsService->getAppDataFolderAbsPath(Application::APP_ID));
			if (isset(ServerService::$APP['userid'])) {
				$cfg->setUserId(ServerService::$APP['userid']);
			}
			$cfg->setUseDBDirect(false);
			$cfg->setUseFileDirect(false);
			$dbCfg = new dbConfig();
			$dbCfg->setDbHost($this->config->getSystemValue('dbhost'));
			$dbCfg->setDbType($this->config->getSystemValue('dbtype'));
			$dbCfg->setDbName($this->config->getSystemValue('dbname'));
			$dbCfg->setDbUser($this->config->getSystemValue('dbuser'));
			$dbCfg->setDbPass($this->config->getSystemValue('dbpassword'));
			$dbCfg->setDbPrefix($this->config->getSystemValue('dbtableprefix'));
			$dbCfg->setIniDbHost(ini_get('mysqli.default_host'));
			$dbCfg->setIniDbPort(ini_get('mysqli.default_port'));
			$dbCfg->setIniDbSocket(ini_get('pdo_mysql.default_socket'));
			$dbdriveroptions = $this->config->getSystemValue('dbdriveroptions');
			if (isset($dbdriveroptions)) {
				$dbCfg->setDbDriverSslKey($dbdriveroptions[\PDO::MYSQL_ATTR_SSL_KEY]);
				$dbCfg->setDbDriverSslCert($dbdriveroptions[\PDO::MYSQL_ATTR_SSL_CERT]);
				$dbCfg->setDbDriverSslCa($dbdriveroptions[\PDO::MYSQL_ATTR_SSL_CA]);
				$dbCfg->setDbDriverSslVerifyCrt($dbdriveroptions[\PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT]);
			}
			$taskInitReply->setDbCfg($dbCfg);
			$taskInitReply->setConfig($cfg);
			if (isset(ServerService::$APP['handler'])) {
				$taskInitReply->setHandler(ServerService::$APP['handler']);
			}
		}
		return $taskInitReply;
	}

	/**
	 * Set task status
	 * 
	 * @param TaskSetStatusRequest $request
	 * 
	 * @return PBEmpty|null
	 */
	public function status(TaskSetStatusRequest $request): ?PBEmpty {
		ServerService::$APP['status'] = $request->getStCode();
		return new PBEmpty(null);
	}

	/**
	 * Task exit
	 * 
	 * @param TaskExitRequest $request
	 * 
	 * @return PBEmpty|null
	 */
	public function exit(TaskExitRequest $request): ?PBEmpty {
		if (isset(ServerService::$APP['handler'])) {
			call_user_func(ServerService::$APP['handler'], ['result' => $request->getResult()]);
		}
		QueriesManager::closeAllQueries(); // Close possible opened cursors on shutdown
		exit(0); // Temporal workaround, because of bad GRPC implementation for PHP
		return new PBEmpty(null);
	}

	/**
	 * Task logging
	 * 
	 * @param TaskLogRequest $request
	 * 
	 * @return PBEmpty|null
	 */
	public function log(TaskLogRequest $request): ?PBEmpty {
		$logLvl = $request->getLogLvl();
		$msg = '';
		foreach ($request->getContent() as $row) {
			$msg .= $row . '\n';
		}
		if ($logLvl === logLvl::DEBUG) {
			$this->logger->debug('[' . $request->getModule() . '] ' . $msg);
		}
		if ($logLvl === logLvl::INFO) {
			$this->logger->info('[' . $request->getModule() . '] ' . $msg);
		}
		if ($logLvl === logLvl::WARN) {
			$this->logger->warning('[' . $request->getModule() . '] ' . $msg);
		}
		if ($logLvl === logLvl::ERROR) {
			$this->logger->error('[' . $request->getModule() . '] ' . $msg);
		}
		if ($logLvl === logLvl::FATAL) {
			$this->logger->emergency('[' . $request->getModule() . '] ' . $msg);
		}
		return new PBEmpty(null);
	}

}