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

namespace OCA\Cloud_Py_API\Service;

use OCP\IConfig;

use OCA\Cloud_Py_API\AppInfo\Application;


class UtilsService {

	/** @var IConfig */
	private $config;

	public function __construct(IConfig $config)
	{
		$this->config = $config;
	}

	/**
	 * Return a suitable PHP interpreter that is likely to be the same version as the
	 * currently running interpreter.  This is similar to using the PHP_BINARY constant, but
	 * it will also work from within mod_php or PHP-FPM, in which case PHP_BINARY will return
	 * unusable interpreters.
	 *
	 * @return string
	 */
	public function getPhpInterpreter() {
		static $cachedExecutable = null;

		if ($cachedExecutable !== null) {
			return $cachedExecutable;
		}

		$basename = basename(PHP_BINARY);

		// If the binary is 'php', 'php7', 'php7.3' etc, then assume it's a usable interpreter
		if ($basename === 'php' || preg_match('/^php\d+(?:\.\d+)*$/', $basename)) {
			return PHP_BINARY;
		}

		// Otherwise, we might be running as mod_php, php-fpm, etc, where PHP_BINARY is not a
		// usable PHP interpreter.  Try to find one with the same version as the current one.

		$candidates = [
			'php' . PHP_MAJOR_VERSION . '.' . PHP_MINOR_VERSION . '.' . PHP_RELEASE_VERSION,
			'php' . PHP_MAJOR_VERSION . '.' . PHP_MINOR_VERSION,
			'php' . PHP_MAJOR_VERSION,
		];

		$envPath = $_SERVER['PATH'] ?? '';
		$paths = $envPath !== '' ? explode(':', $envPath) : [];

		if (!in_array(PHP_BINDIR, $paths, true)) {
			$paths[] = PHP_BINDIR;
		}

		foreach ($candidates as $candidate) {
			foreach ($paths as $path) {
				$executable = $path . DIRECTORY_SEPARATOR . $candidate;
				if (is_executable($executable)) {
					$cachedExecutable = $executable;
					return $executable;
				}
			}
		}

		// Fallback, if nothing else can be found
		$cachedExecutable = 'php';
		return $cachedExecutable;
	}

	/**
	 * Check if a php function available
	 * 
	 * @param string $function_name
	 * 
	 * @return bool
	 */
	private function isFunctionEnabled($function_name) {
		if (!function_exists($function_name)) {
			return false;
		}
		/** @var IniGetWrapper $ini */
		$ini = \OC::$server->get(IniGetWrapper::class);
		$disabled = explode(',', $ini->get('disable_functions') ?: '');
		$disabled = array_map('trim', $disabled);
		if (in_array($function_name, $disabled)) {
			return false;
		}
		$disabled = explode(',', $ini->get('suhosin.executor.func.blacklist') ?: '');
		$disabled = array_map('trim', $disabled);
		if (in_array($function_name, $disabled)) {
			return false;
		}
		return true;
	}

	public function getCustomAppsDirectory() {
		$apps_directory = $this->config->getSystemValue('apps_paths');
		if ($apps_directory !== "" && is_array($apps_directory) && count($apps_directory) > 0) {
			foreach ($apps_directory as $custom_apps_dir) {
				$appDir = $custom_apps_dir['path'] . '/' . Application::APP_ID;
				if (file_exists($custom_apps_dir['path']) && is_dir($custom_apps_dir['path']) && $custom_apps_dir['writable'] 
					&& file_exists($appDir) && is_dir($appDir)) {
					return $custom_apps_dir['path'] . '/';
				}
			}
		}
		return getcwd() . '/apps/';
	}

}